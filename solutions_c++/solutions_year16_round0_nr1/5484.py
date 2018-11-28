#include <bits/stdc++.h>

using namespace std;

long long _();
int main() { _(); return 0; }
#define main _
#define int long long 

int main()
{
   ios_base::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int test=1; test<=T; test++)
   {
      bool t[10] = {0};
      int c = 0;
      int n;
      cin >> n;
      if(n == 0)
      {
         cout << "Case #" << test << ": INSOMNIA" << endl;
         continue;
      }
      int r = 0;
      while(c < 10)
      {
         r += n;
         int x = r;
         while(x)
         {
            if(!t[x % 10])
            {
               c++;
               t[x % 10] = 1;
            }
            x /= 10;
         }
      }
      cout << "Case #" << test << ": " << r << endl;
   }
   return 0;
}