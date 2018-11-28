#include<iostream>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;



main()
{

int T;
int A, B, K;

int i, j,k;

cin>> T;

for( i = 0; i<T; i++)
{
   int count = 0;
   cin>> A >> B >> K;

  // printf("A : %d,  B : %d , K : %d\n", A, B, K);
   for( j = 0; j<A; j++)
   {
      for( k = 0; k<B; k++)
      {
       int res = j&k;
       //printf("%d & %d : %d\n", j, k, (j&k));
       if ( res < K) count++;
      }
   }

   printf("Case #%d: %d\n", i+1, count); 

}

}

