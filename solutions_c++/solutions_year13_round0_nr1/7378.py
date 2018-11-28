#include <stdio.h>

bool checkBoard(char* board, char player) {
  bool won=false;
  for(int i=0;i<4;i++) {
    bool consistent = true;
    for(int j=0;j<4;j++) {
      consistent &= board[i*4+j] == player || board[i*4+j] == 'T';
    }
    won |= consistent;
    if (won) {
      return true;
    }
    consistent = true;
    for(int j=0;j<4;j++) {
      consistent &= board[i+4*j] == player || board[i+4*j] == 'T';
    }
    won |= consistent;
    if (won) {
      return true;
    }
  }
  if (won) {
    return true;
  }
  won = true;
  for(int i=0;i<4;i++) {
    won &= board[i*4+i] == player || board[i*4+i] == 'T';
  }
  if (won) {
    return true;
  }
  won = true;
  for(int i=0;i<4;i++) {
    won &= board[i*3+3] == player || board[i*3+3] == 'T';
  }
  return won;
}

bool hasEmpty(char* board) {
  for(int i=0;i<16;i++) {
    if (board[i] == '.') {
      return true;
    }
  }
  return false;
}

int main(int argc, char** argv) {
  int n;
  scanf("%d",&n);
  char* boards = new char[16*n];
  getchar();
  for(int i=0;i<n;i++) {
    char* board = boards+16*i;
    for(int j=0;j<4;j++) {
      for(int k=0;k<4;k++) {
        board[j*4+k]=getchar();
      }
      getchar();
    }
    getchar();
  }
  for(int i=0;i<n;i++) {
    char* board = boards+i*16;
    char result = checkBoard(board,'X') ? 'X' : checkBoard(board,'O') ? 'O' : hasEmpty(board) ? 'G' : 'D';
    printf("Case #%d: ",i+1);
    switch(result) {
      case 'X':
      case 'O':
        printf("%c won",result);
        break;
      case 'D':
        printf("Draw");
        break;
      case 'G':
        printf("Game has not completed");
        break;
    }
    putchar('\n');
  }
  /*
  printf("num: %d\n",n);
  for(int i=0;i<n;i++) {
    for(int j=0;j<4;j++) {
      for(int k=0;k<4;k++) {
        putchar(boards[i*16+j*4+k]);
      }
      putchar('\n');
    }
    putchar('\n');
  }
  */
  return 0;
}
