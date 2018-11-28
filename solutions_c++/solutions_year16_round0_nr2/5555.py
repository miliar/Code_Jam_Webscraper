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
      string s;
      cin >> s;
      int r = 0;
      for(int i=0; i<s.size()-1; i++)
         r += s[i] != s[i+1];
      r += s.back() == '-';
      cout << "Case #" << test << ": " << r << endl;
   }
   return 0;
}