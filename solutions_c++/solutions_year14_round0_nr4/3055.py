#include<stdio.h>
#include<stdlib.h>

int cmp(const void *a, const void *b)
{
   double n1 = *(double *)a;
   double n2 = *(double *)b;
   if( n1 > n2 )   return 1;
   else if( n1 < n2 )   return -1;
   return 0;
}

int WAR(int N, double *a, double *b)
{
   int i, aI=0, bI=0;
   while( aI<N && bI<N )
   {
      if( b[bI] > a[aI] )   aI++;
      bI++;
   }
   return N-aI;
}

int main()
{
   int T, t=0, N, i, j;
   double block[2][1000];

   scanf("%d",&T);
   while( t++ < T )
   {
      scanf("%d",&N);
      for( i=0; i<N; i++ )   scanf("%lf",block[0]+i);
      for( i=0; i<N; i++ )   scanf("%lf",block[1]+i);

      qsort(block[0], N, sizeof(double), cmp);
      qsort(block[1], N, sizeof(double), cmp);
      printf("Case #%d: %d %d\n", t, N-WAR(N,block[1],block[0]), WAR(N,block[0],block[1]));
   }
   return 0;
}
