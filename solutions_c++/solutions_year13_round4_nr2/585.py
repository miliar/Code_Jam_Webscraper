#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <string.h>
#include <math.h>

int N;
__int64 P;

__int64 Solver(int N, __int64 P){
   __int64 NN, res;

   NN = (__int64)1 << (N-1);
   res = 1;
   while( NN < P ){
      res = 2 * res + 1;
      NN = NN / 2 + ( (__int64)1 << (N-1) );
   }

   return res;
}

__int64 Solver1(int N, __int64 P){
   __int64 NN, res, sub;

   NN = (__int64)1 << N;
   res = (__int64)1 << N;
   sub = 1;
   while( NN > P ){
      res = res - sub;
      sub = sub * 2;
      NN = NN >> 1;
   }

   return res;
}

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T, t;
  __int64 res1, res2;

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
    fscanf(filein, "%d %I64d\n", &N, &P);
    printf("%d %I64d\n", N, P);

    // Solve & Output
    if( P == ((__int64)1 << N) ){
       fprintf(fileout, "Case #%d: %I64d %I64d\n", t + 1, P-1, P-1);
    }
    else{
       res1 = Solver(N, P);
//       res2 = Solver(N, ((__int64)1 << N) - P);
       res2 = Solver1(N, P);
//       fprintf(fileout, "Case #%d: %I64d %I64d\n", t + 1, res1-1, ((__int64)1 << N) - res2 - 1);
       fprintf(fileout, "Case #%d: %I64d %I64d\n", t + 1, res1-1, res2-1);
    }
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
