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
      int b, m;
      cin >> b >> m;
      bool ok = 1;
      string s(b, '0');
      for(int i=b-1; m && i >= 1; i--, m/=2)
         s[i] += m % 2;
      ok = !m;
      if(s[1] == '1')
      {
         for(int i=2; i<b; i++)
            if(s[i] == '1')
               ok = 0;
         if(ok)
            for(int i=2; i<b; i++)
               s[i] = '1';
      }
      else
      {
         for(int i=1; i<b-1; i++)
            s[i] = s[i+1];
         s[b-1] = '0';
      }
      cout << "Case #" << test << ": " << (ok ? "" : "IM") << "POSSIBLE" << endl;
      if(!ok)
         continue;
      cout << s << endl;
      for(int i=0; i<b-1; i++)
      {
         for(int j=0; j<b; j++)
            cout << (char) ('0' + (j > i+1));
         cout << endl;
      }
   }
   return 0;
}