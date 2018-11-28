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
      int n;
      cin >> n;
      priority_queue<pair<int, char>> p;
      int s = 0;
      for(int i=0; i<n; i++)
      {
         int x;
         cin >> x;
         p.push({x, 'A' + i});
         s += x;
      }
      cout << "Case #" << test << ": ";
      while(s)
      {
         auto x = p.top();
         p.pop();
         auto y = p.top();
         p.pop();
         if(s == 3 && p.size() == 1)
         {
            auto z = p.top();
            p.pop();
            cout << x.second << " " << y.second << z.second;
            s -= 3;
         }
         else 
         {
            if(x.first > y.first+1)
            {
               cout << x.second << x.second << " ";
               x.first -= 2;
            }
            else
            {
               cout << x.second << y.second << " ";
               x.first--;
               y.first--;
            }
            p.push(x);
            p.push(y);
            s -= 2;
         }
      }
      cout << endl;
   }
   return 0;
}