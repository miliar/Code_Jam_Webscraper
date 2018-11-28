#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char A[100][100];

int Check(int R, int r, int C, int c){
  for( int k = 0; k < R; k ++ ){
    if( k == r ){
      continue;
    }
    if( A[k][c] != '.' ){
      return 0;
    }
  }
  for( int k = 0; k < C; k ++ ){
    if( k == c ){
      continue;
    }
    if( A[r][k] != '.' ){
      return 0;
    }
  }
  return 1;
}

int Solver(int R, int C){
  int i, j, k, f, res = 0;
  for( i = 0; i < R; i ++ ){
    for( j = 0; j < C; j ++ ){
      f = 0;
      switch(A[i][j]){
      case '.':
        break;
      case '^':
        for( k = i - 1; k >= 0; k -- ){
          if( A[k][j] != '.' ){
            f = 1;
            break;
          }
        }
        if( f == 1 ){
          break;
        }
        if( Check(R, i, C, j) ){
          return -1;
        }
        else{
          res ++;
        }
        break;
      case 'v':
        for( k = i + 1; k < R; k ++ ){
          if( A[k][j] != '.' ){
            f = 1;
            break;
          }
        }
        if( f == 1 ){
          break;
        }
        if( Check(R, i, C, j) ){
          return -1;
        }
        else{
          res ++;
        }
        break;
      case '<':
        for( k = j - 1; k >= 0; k -- ){
          if( A[i][k] != '.' ){
            f = 1;
            break;
          }
        }
        if( f == 1 ){
          break;
        }
        if( Check(R, i, C, j) ){
          return -1;
        }
        else{
          res ++;
        }
        break;
      case '>':
        for( k = j + 1; k < C; k ++ ){
          if( A[i][k] != '.' ){
            f = 1;
            break;
          }
        }
        if( f == 1 ){
          break;
        }
        if( Check(R, i, C, j) ){
          return -1;
        }
        else{
          res ++;
        }
        break;
      }
    }
  }

  return res;
}

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T;
  int t, i, j, R, C, res;

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
    fscanf(filein, "%d %d\n", &R, &C);
    printf("%d %d\n", R, C);
    for( i = 0; i < R; i ++ ){
      for( j = 0; j < C; j ++ ){
        fscanf(filein, "%c", &(A[i][j]));
        printf("%c", A[i][j]);
      }
      fscanf(filein, "\n");
      printf("\n");
    }

    // Solve & Output
    res = Solver(R,C);
    if( res == -1 ){
      fprintf(fileout, "Case #%d: IMPOSSIBLE\n", t + 1);
    }
    else{
      fprintf(fileout, "Case #%d: %d\n", t + 1, res);
    }
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
