#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N;
double a[1000];
double b[1000];

int f()
{
   int i = 0;
   for(int j = 0; i + j < N; i++)
   {
      while(i + j < N && b[j] < a[i+j])
         j++;
      if(i + j == N)
         break;
   }
   return N - i;
}

int g()
{
   int i = 0;
   for(int j = 0; i < N && j < N; i++, j++)
   {
      while(j < N && b[j] < a[i])
         j++;
      if(j == N)
         break;
   }
   return N - i;
}

int main()
{
   int nbTests;
   cin >> nbTests;
   for(int test=1; test<=nbTests; test++)
   {
      cin >> N;
      for(int i=0; i<N; i++)
         cin >> a[i];
      for(int i=0; i<N; i++)
         cin >> b[i];
      sort(a, a + N);
      sort(b, b + N);
      cout << "Case #" << test << ": " << f() << " " << g() << endl;
   }
   return 0;
}