#include <bits/stdc++.h>

using namespace std;

long long _();
int main() { _(); return 0; }
#define main _
#define int long long 

int n;
char v[100];

string f(int p, char c)
{
   if(p)
   {
      string a = f(p-1, v[c]);
      string b = f(p-1, c);
      return a < b ? a + b : b + a;
   }
   return string(1, c);
}

bool ok(string& str, int r, int p, int s)
{
   for(char c : str)
   {
      if(c == 'R')
         r--;
      if(c == 'P')
         p--;
      if(c == 'S')
         s--;
   }
   return r == 0 && p == 0 && s == 0;
}

string g(int r, int p, int s)
{
   string t = "RPS";
   for(char c : t)
   {
      string str = f(n, c);
      //cout << str << endl;
      if(ok(str, r, p, s))
         return str;
   }
   return "IMPOSSIBLE";
}

int main()
{
   v['R'] = 'S';
   v['P'] = 'R';
   v['S'] = 'P';
   ios_base::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int test=1; test<=T; test++)
   {
      int r, p, s;
      cin >> n >> r >> p >> s;
      string str = g(r, p, s);
      cout << "Case #" << test << ": " << str << endl;
   }
   return 0;
}