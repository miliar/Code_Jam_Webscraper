#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N, M;
int t[100][100];
int u[100][100];

bool f()
{
   for(int i=0; i<N; i++)
      for(int j=0; j<M; j++)
         u[i][j] = 100;
   for(int i=0; i<N; i++)
   {
      int m = 0;
      for(int j=0; j<M; j++)
         m = max(m, t[i][j]);
      for(int j=0; j<M; j++)
         u[i][j] = min(u[i][j], m);
   }
   for(int j=0; j<M; j++)
   {
      int m = 0;
      for(int i=0; i<N; i++)
         m = max(m, t[i][j]);
      for(int i=0; i<N; i++)
         u[i][j] = min(u[i][j], m);
   }
   for(int i=0; i<N; i++)
      for(int j=0; j<M; j++)
         if(t[i][j] != u[i][j])
            return false;
   return true;
}

int main()
{
   int nbTests;
   scanf("%d", &nbTests);
   for(int test=1; test<=nbTests; test++)
   {
      scanf("%d%d", &N, &M);
      for(int i=0; i<N; i++)
         for(int j=0; j<M; j++)
            scanf("%d", &t[i][j]);
      printf("Case #%d: %s\n", test, f() ? "YES" : "NO");
   }
   return 0;
}