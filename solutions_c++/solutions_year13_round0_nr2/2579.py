#include <iostream>
#include <cstdio>
#include <fstream>

using namespace std;

#define Nmax 101
#define amax 101

int arr[Nmax][Nmax];
int maxR[Nmax], maxC[Nmax];

bool findRes(int N, int M) {
   int i, j;
   
   for(i=0; i<N; i++) {
      maxR[i] = 0;
      for(j=0; j<M; j++) 
         if(arr[i][j] > maxR[i])
            maxR[i] = arr[i][j];
   }
   
   for(j=0; j<M; j++) {
      maxC[j] = 0;
      for(i=0; i<N; i++)
         if(arr[i][j] > maxC[j])
            maxC[j] = arr[i][j];
   }
   
   for(i=0; i<N; i++)
      for(j=0; j<M; j++)
         if(arr[i][j] != maxR[i] && arr[i][j] != maxC[j])
            return false;
   return true;
}

int main(void) {
   freopen("B-large.in", "r", stdin);
   freopen("lawnmowerB.out", "w", stdout);
   int T, N, M;
   int i, j, k;
   bool res;
   
   scanf("%d", &T);
   //printf("%d\n", T);
   
   for(k=1; k<=T; k++) {
      scanf("%d %d", &N, &M);
      
      for(i=0; i<N; i++)
         for(j=0; j<M; j++)
            scanf("%d", &arr[i][j]);
      res = findRes(N, M);
      
      printf("Case #%d: ", k);
      if(res == true)
         printf("YES");
      else
         printf("NO");
      printf("\n");
   }
   
   return 0;
}
            
      
