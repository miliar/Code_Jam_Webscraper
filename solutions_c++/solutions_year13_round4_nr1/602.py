#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <string.h>
#include <math.h>

int N, M, o[1001], e[1001], p[1001], p1[1001];

int Solver(void){
   __int64 Cost1, Cost2;
   int i, j, tmp, sto[1001], stp[1001], top;
   bool flag;

   Cost1 = 0;
   for( i = 0; i < M; i ++ ){
      Cost1 = (Cost1 + (__int64) (N + (N - (e[i] - o[i] - 1))) * (e[i] - o[i]) / 2 * p[i]) % 1000002013;
   }

   for( i = 0; i < M; i ++ ){
      p1[i] =p [i];
   }

   flag = true;
   while( flag ){
      flag = false;
      for( i = 0; i < M - 1; i ++ ){
         if( o[i] > o[i+1] ){
            tmp = o[i];
            o[i] = o[i+1];
            o[i+1] = tmp;
            tmp = p[i];
            p[i] = p[i+1];
            p[i+1] = tmp;
            flag = true;
         }
      }
   }
   flag = true;
   while( flag ){
      flag = false;
      for( i = 0; i < M - 1; i ++ ){
         if( e[i] > e[i+1] ){
            tmp = e[i];
            e[i] = e[i+1];
            e[i+1] = tmp;
            tmp = p1[i];
            p1[i] = p1[i+1];
            p1[i+1] = tmp;
            flag = true;
         }
      }
   }

   o[M] = N+1;
   e[M] = N+1;
   top = -1;
   i = 0;
   j = 0;
   Cost2 = 0;
   while( i + j < 2 * M ){
      if( o[i] <= e[j] ){
         top ++;
         sto[top] = o[i];
         stp[top] = p[i];
         i ++;
      }
      else{
         while( p1[j] > 0 ){
            if( stp[top] > p1[j] ){
               stp[top] -= p1[j];
               Cost2 = (Cost2 + (__int64) (N + (N - (e[j] - sto[top] - 1))) * (e[j] - sto[top]) / 2 * p1[j]) % 1000002013;
               p1[j] = 0;
            }
            else{
               p1[j] -= stp[top];
               Cost2 = (Cost2 + (__int64) (N + (N - (e[j] - sto[top] - 1))) * (e[j] - sto[top]) / 2 * stp[top]) % 1000002013;
               top --;
            }
         }
         j ++;
      }
   }

   Cost1 = ((Cost1 + 1000002013) - Cost2) % 1000002013;

   return Cost1;
}

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int T, m;
  int res, t;

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
    fscanf(filein, "%d %d\n", &N, &M);
    printf("%d %d\n", N, M);
    for( m = 0; m < M; m ++ ){
      fscanf(filein, "%d %d %d\n", o+m, e+m, p+m);
      printf("%d %d %d\n", o[m], e[m], p[m]);
    }

    // Solve & Output
    res = Solver();
    fprintf(fileout, "Case #%d: %d\n", t + 1, res);
  }

  fclose(fileout);
  fclose(filein);

  return 0;
}
