#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char SR[13][4096], SP[13][4096], SS[13][4096], tmp[4096];
int CRR[12], CRP[12], CRS[12], CPR[12], CPP[12], CPS[12], CSR[12], CSP[12], CSS[12];
int C[3][13][3];

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T;
  int t, N, R, P, S, i, j, k;

  if( argc < 3 ){
    printf("Usage is: task1 filein fileout\n");
    return 0;
  }

  SR[0][0] = 'R';
  SP[0][0] = 'P';
  SS[0][0] = 'S';
  for( i = 0; i < 3; i ++ )
    for( j = 0; j < 13; j ++ )
      for( k = 0; k < 3; k ++ )
        C[i][j][k] = 0;

  C[0][0][0] = 1;
  C[1][0][1] = 1;
  C[2][0][2] = 1;
  for( i = 0; i < 12; i ++ ){
    for( j = 0; j < (1 << i); j ++ ){
      if( SR[i][j] == 'R' ){
        SR[i+1][2*j] = 'R';
        SR[i+1][2*j+1] = 'S';
        C[0][i+1][0] ++;
        C[0][i+1][2] ++;
      }
      if( SR[i][j] == 'P' ){
        SR[i+1][2*j] = 'P';
        SR[i+1][2*j+1] = 'R';
        C[0][i+1][0] ++;
        C[0][i+1][1] ++;
      }
      if( SR[i][j] == 'S' ){
        SR[i+1][2*j] = 'P';
        SR[i+1][2*j+1] = 'S';
        C[0][i+1][1] ++;
        C[0][i+1][2] ++;
      }

      if( SP[i][j] == 'R' ){
        SP[i+1][2*j] = 'R';
        SP[i+1][2*j+1] = 'S';
        C[1][i+1][0] ++;
        C[1][i+1][2] ++;
      }
      if( SP[i][j] == 'P' ){
        SP[i+1][2*j] = 'P';
        SP[i+1][2*j+1] = 'R';
        C[1][i+1][0] ++;
        C[1][i+1][1] ++;
      }
      if( SP[i][j] == 'S' ){
        SP[i+1][2*j] = 'P';
        SP[i+1][2*j+1] = 'S';
        C[1][i+1][1] ++;
        C[1][i+1][2] ++;
      }

      if( SS[i][j] == 'R' ){
        SS[i+1][2*j] = 'R';
        SS[i+1][2*j+1] = 'S';
        C[2][i+1][0] ++;
        C[2][i+1][2] ++;
      }
      if( SS[i][j] == 'P' ){
        SS[i+1][2*j] = 'P';
        SS[i+1][2*j+1] = 'R';
        C[2][i+1][0] ++;
        C[2][i+1][1] ++;
      }
      if( SS[i][j] == 'S' ){
        SS[i+1][2*j] = 'P';
        SS[i+1][2*j+1] = 'S';
        C[2][i+1][1] ++;
        C[2][i+1][2] ++;
      }
    }
  }

  for( i = 2; i < 13; i ++ ){
    for( j = 2; j < (1 << i); j = j * 2 ){
      for( k = 0; k < (1 << i); k += 2 * j ){
        if( strncmp(SR[i]+k,SR[i]+k+j,j) > 0 ){
          strncpy(tmp,SR[i]+k,j);
          strncpy(SR[i]+k,SR[i]+k+j,j);
          strncpy(SR[i]+k+j,tmp,j);
        }
        if( strncmp(SP[i]+k,SP[i]+k+j,j) > 0 ){
          strncpy(tmp,SP[i]+k,j);
          strncpy(SP[i]+k,SP[i]+k+j,j);
          strncpy(SP[i]+k+j,tmp,j);
        }
        if( strncmp(SS[i]+k,SS[i]+k+j,j) > 0 ){
          strncpy(tmp,SS[i]+k,j);
          strncpy(SS[i]+k,SS[i]+k+j,j);
          strncpy(SS[i]+k+j,tmp,j);
        }
      }
    }
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
    fscanf(filein, "%d %d %d %d\n", &N, &R, &P, &S);
    printf("%d %d %d %d\n", N, R, P, S);

    // Solve & Output

    if( ( R == C[0][N][0] )&&( P == C[0][N][1] )&&( S == C[0][N][2] ) ){
      fprintf(fileout, "Case #%d: ", t + 1);
      for( i = 0; i < (1 << N); i ++ ){
        fprintf(fileout, "%c", SR[N][i]);
      }
    }
    else
    if( ( R == C[1][N][0] )&&( P == C[1][N][1] )&&( S == C[1][N][2] ) ){
      fprintf(fileout, "Case #%d: ", t + 1);
      for( i = 0; i < (1 << N); i ++ ){
        fprintf(fileout, "%c", SP[N][i]);
      }
    }
    else
    if( ( R == C[2][N][0] )&&( P == C[2][N][1] )&&( S == C[2][N][2] ) ){
      fprintf(fileout, "Case #%d: ", t + 1);
      for( i = 0; i < (1 << N); i ++ ){
        fprintf(fileout, "%c", SS[N][i]);
      }
    }
    else
      fprintf(fileout, "Case #%d: IMPOSSIBLE", t + 1);

    fprintf(fileout, "\n");
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}


    //for( i = 0; i < 12; i ++ ){
    //  CR[i] = 0;
    //  CP[i] = 0;
    //  CS[i] = 0;
    //  for( j = 0; j < (1 << i); j ++ ){
    //    if( SR[i][j] == 'R' ){
    //      CR[i] ++;
    //    }
    //    if( SR[i][j] == 'P' ){
    //      CR[i] ++;
    //    }
    //    if( SR[i][j] == 'S' ){
    //      CR[i] ++;
    //    }
    //  }
    //}

