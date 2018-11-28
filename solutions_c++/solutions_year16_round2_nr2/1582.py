#include <bits/stdc++.h>

using namespace std;

long long _();
int main() { _(); return 0; }
#define main _
#define int long long 

string a, b;

vector<int> f(string s)
{
   while(s.size() < 3)
      s = "0" + s;
   vector<int> r;
   for(int i=0; i<=9; i++)
      for(int j=0; j<=9; j++)
         for(int k=0; k<=9; k++)
            if((s[0]-'0' == i || s[0] == '?') && (s[1]-'0' == j || s[1] == '?') && (s[2]-'0' == k || s[2] == '?'))
               r.push_back(100*i+10*j+k);
   return r;
}

int main()
{
   ios_base::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int test=1; test<=T; test++)
   {
      cin >> a >> b;
      vector<int> x = f(a);
      vector<int> y = f(b);
      int bv = 1e4, bi, bj;
      for(int i : x)
         for(int j : y)
            if(abs(i - j) < bv)
            {
               bv = abs(i - j);
               bi = i;
               bj = j;
            }
      cout << "Case #" << test << ": " << setfill('0') << setw(a.size()) << bi << " " << setfill('0') << setw(a.size()) << bj << endl;
   }
   return 0;
}