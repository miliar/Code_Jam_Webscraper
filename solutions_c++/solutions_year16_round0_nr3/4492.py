#include <bits/stdc++.h>

using namespace std;

long long _();
int main() { _(); return 0; }
#define main _
#define int long long 

int h(int n)
{
   for(int i=2; i*i <= n; i++)
      if(n % i == 0)
         return i;
   return 0;
}

string g(int n)
{
   string r;
   while(n)
   {
      r += '0' + n % 2;
      n /= 2;
   }
   reverse(r.begin(), r.end());
   return r;
}

vector<int> f(int n)
{
   vector<int> r;
   for(int i=2; i<=10; i++)
   {
      int m = n;
      int b = 1;
      int v = 0;
      while(m)
      {
         v += (m % 2) * b;
         b *= i;
         m /= 2;
      }
      int x = h(v);
      if(!x)
         return vector<int>();
      r.push_back(x);
   }
   return r;
}

int main()
{
   ios_base::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int test=1; test<=T; test++)
   {
      int n, j;
      cin >> n >> j;
      int i = (1LL << n-1) + 1;
      vector<int> r;
      while(r.size() < j)
      {
         if(f(i).size())
            r.push_back(i);
         i += 2;
      }
      cout << "Case #" << test << ":" << endl;
      for(int a : r)
      {
         cout << g(a) << " ";
         vector<int> v = f(a);
         for(int x : v)
            cout << x << " ";
         cout << endl;
      }
   }
   return 0;
}