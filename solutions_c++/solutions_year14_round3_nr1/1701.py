#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <string.h>
#include <math.h>

__int64 NOD(__int64 A, __int64 B){
  __int64 r;
  r = A % B;
  if( r == 0 ){
    return B;
  }
  else{
    return NOD(B, r);
  }
}

int Solver(__int64 P, __int64 Q){
  __int64 nod = NOD(Q, P);
  int res = 0;
  int i, possible = 0;

  printf("nod=%I64d\n", nod);
  P = P / nod;
  Q = Q / nod;

  for( i = 0; i < 41; i ++ ){
    if( Q == (1 << i) ){
      possible = 1;
      break;
    }
  }

  if( possible == 0 ){
    return 0;
  }

  while( P < Q ){
    res ++;
    P *= 2;
  }

  return res;
}

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T;
  int res, t, i;
  __int64 P, Q;

  if( argc < 3 ){
    printf("Usage is: TaskA filein fileout\n");
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
    fscanf(filein, "%I64d/%I64d\n", &P, &Q);
    printf("%I64d/%I64d\n", P, Q);
    // Solve & Output

    res = Solver(P, Q);
    if( res == 0 ){
      fprintf(fileout, "Case #%d: impossible\n", t + 1);
    }
    else{
      fprintf(fileout, "Case #%d: %d\n", t + 1, res);
    }
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
