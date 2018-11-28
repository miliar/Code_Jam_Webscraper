#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char S[2001];
char D[10][6] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int Count[26], Digs[10], len;

void Solver(FILE* f){
  int i, j;

  for( i = 0; i < 26; i ++ ){
    Count[i] = 0;
  }
  for( i = 0; i < 10; i ++ ){
    Digs[i] = 0;
  }

  len = strlen(S);
  printf("len=%d\n",len);
  for( i = 0; i < len; i ++ ){
    Count[S[i]-'A'] ++;
  }
  Digs[0] = Count['Z'-'A'];
  Digs[2] = Count['W'-'A'];
  Digs[4] = Count['U'-'A'];
  Digs[6] = Count['X'-'A'];
  Digs[8] = Count['G'-'A'];
  for( i = 0; i < 10; i ++ ){
    for( j = 0; j < strlen(D[i]); j ++ ){
      Count[D[i][j]-'A'] -= Digs[i];
    }
  }
  Digs[1] = Count['O'-'A'];
  Digs[3] = Count['H'-'A'];
  Digs[5] = Count['F'-'A'];
  Digs[7] = Count['S'-'A'];
  Digs[9] = Count['I'-'A'] - Count['F'-'A'];

  for( i = 0; i < 10; i ++ ){
    for( j = 0; j < Digs[i]; j ++ ){
      fprintf(f, "%c", '0' + i);
    }
  }
  fprintf(f, "\n");
  return;
}

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T;
  int t;

  if( argc < 3 ){
    printf("Usage is: task1 filein fileout\n");
    return 0;
  }

  // Input 

  filein = fopen(argv[1], "r");
  if( filein == NULL ){
    printf("Error open(); filein\n");
    return 0;
  }
  fileout = fopen(argv[2], "w");
  if( fileout == NULL ){
    printf("Error open(); fileout\n");
    return 0;
  }

  fscanf(filein, "%d\n", &T);
  printf("%d\n", T);
  for( t = 0; t < T; t ++ ){
    printf("-------------\t=%d\n", t);
    fscanf(filein, "%s\n", S);
    printf("%s\n", S);

    // Solve & Output
    fprintf(fileout, "Case #%d: ", t + 1);
    Solver(fileout);
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
