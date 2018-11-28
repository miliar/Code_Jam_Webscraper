#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int N;
int t[100];

int f(int i, int c, int v)
{
   if(i == N)
      return c;
   if(v == 1)
      return N;
   if(v > t[i])
      return f(i+1, c, v + t[i]);
   int n = 1 + (int) (log((t[i]-1) / (double) (v-1)) / log(2.0));
   v = pow(2.0, n) * (v - 1) + 1 + t[i];
   return min(f(i+1, c+n, v), c + N-i);
}

int main()
{
   int nbTests;
   cin >> nbTests;
   for(int test=1; test<=nbTests; test++)
   {
      int A;
      cin >> A >> N;
      for(int i=0; i<N; i++)
         cin >> t[i];
      sort(t, t+N);
      cout << "Case #" << test << ": " << f(0, 0, A) << "\n";
   }
   return 0;
}