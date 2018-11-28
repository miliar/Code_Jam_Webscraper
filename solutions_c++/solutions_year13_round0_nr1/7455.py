#include <cstdio>
#include <cstdlib>

char board[4][4];
int complete=1;
FILE *fp;

int status();
int readboard();
int gameloop();

int readboard() {
  char buffer[20];
  for (int i = 0; i < 4; ++i) {
    fscanf(fp, "%s", &buffer);
    for (int j = 0; j < 4; ++j) {
      board[i][j]=buffer[j];
      //printf("%c", board[i][j]);
    }
    //printf("\n");
  }
  return 0;
}

int analyse(char test) {
  switch(test) {
  case '.': complete=0; break;
  case 'O': return 10; break;
  case 'X': return 100; break;
  case 'T': return 1000; break;
  };
  return 0;
}

int decide(int sum) {
  switch(sum){
  case 1030:
  case 40:
    printf("O won");
    return 1;

  case 1300:
  case 400:
    printf("X won");
    return 1;
  };
  return 0;
}

int status() {
  int wflag=1;
  int rsum=0;
  int csum=0;
  int rdia=0;
  int ldia=0;
  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      rsum+=analyse(board[i][j]);
      csum+=analyse(board[j][i]);
      if(i==j) rdia+=analyse(board[i][j]);
      if(3-i==j) ldia+=analyse(board[i][j]);
    }
    if(decide(rsum)) return 1;
    if(decide(csum)) return 1;
    if(decide(rdia)) return 1;
    if(decide(ldia)) return 1;
    rsum=0;
    csum=0;
  }

  if(complete==0)
    printf("Game has not completed");
  else
    printf("Draw");

  return 0;
}

int gameloop() {
  int count;
  fscanf(fp, "%d", &count);
  // printf("%d\n", count);
  for (int i = 0; i < count; ++i) {
    readboard();
    printf("Case #%d: ", i+1);
    status();
    printf("\n");
    complete=1;
  }
}

int main(int argc, char *argv[]) {
  if(argc>1) fp=fopen(argv[1], "r");
  else {
    printf("ERROR: missing argument\n");
    exit(1); //TODO: Learn escape codes
  }

  if(!fp) {
    printf("ERROR: %s isn't the plain text file\n", argv[1]);
    exit(2);
  }

  gameloop();
  fclose(fp);
  return 0;
}
