#include <cstdio>

int T;
int lawn[100][100];

void f(int test)
{
      int N, M;
      scanf("%d%d", &N, &M);
      for(int i=0; i<N; i++)
         for(int j=0; j<M; j++)
            scanf("%d", &lawn[i][j]);
      for(int h=1; h<=100; h++)
      {
         int nb1[100], nb2[100];
         for(int i=0; i<N; i++)
         {
            nb1[i] = 0;
            for(int j=0; j<M; j++)
               if(lawn[i][j] == h) nb1[i]++;
        //    printf("%d %d %d\n", h, i, nb1);
         }
         for(int i=0; i<M; i++)
         {
            nb2[i] = 0;
            for(int j=0; j<N; j++)
               if(lawn[j][i] == h) 
                  nb2[i]++;
         }
         for(int i=0; i<N; i++)
            for(int j=0; j<M; j++)
               if(lawn[i][j] == h)
               {
                  lawn[i][j]++;
                  if( (nb1[i] > 0 && nb1[i] < M) && (nb2[j] > 0 && nb2[j] < N))
                  {
                     printf("Case #%d: NO\n", test);
                     return;
                  }
               }
      }
      printf("Case #%d: YES\n", test);
}

int main()
{
   scanf("%d", &T);
   for(int test=1; test<=T; test++)
      f(test);
   return 0;
}
