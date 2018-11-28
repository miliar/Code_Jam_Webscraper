#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
   long long T;
   scanf("%lld", &T);
   long long A[T], B[T], K[T];
   for(long long i = 0; i < T; i ++)
   {
      scanf("%lld%lld%lld", &A[i], &B[i], &K[i]);
   }

   for(long long i = 0; i < T; i ++)
   {
      long long counter = 0;
      for(long long j = 0; j < A[i]; j ++)
      {
         for(long long k = 0; k < B[i]; k ++)
         {
            long long x = j & k;
            if (x < K[i] && x >= 0)
               counter ++;
         }
      }

      printf("Case #%lld: %lld\n", i + 1, counter);
   }

   return 0;
}
