#include<bits/stdc++.h>
using namespace std;
# ifdef DEB
# define debug(...) fprintf(stderr, __VA_ARGS__)
# else
# define debug(...)
#endif
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define LL long long
#define LD long double
#define PII pair<int, int>
#define PLL pair<LL, LL>
#define pb pop_back
#define VI vector<int> 
#define VPI vector<PII> 
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define RE(i,n) FOR(i,1,n)
#define REP(i,n) FOR(i,0,(int)(n)-1)
#define ALL(x) (x).begin(), (x).end()
#define siz(V) ((int)V.size())


void solve(int ind)
{
  int k, res = 0;
  string s;
  cin>> s >> k;
  for (int i = 0; i <= siz(s) - k; i++)
  {
    if (s[i] == '-')
    {
      for (int j = i; j < i + k; j++)
      {
        if (s[j] == '-')
        {
          s[j] = '+';
        }
        else
        {
          s[j] = '-';
        }
      }
      res++;
    }
  }
  for (int i = 0; i < siz(s); i++)
  {
    if (s[i] == '-')
    {
      res = -1;
    }
  }
 // cout<< s << '\n';
  if (res == -1)
  {
    cout<< "Case #" << ind << ": IMPOSSIBLE\n";
  }
  else
  {
    cout<< "Case #" << ind << ": " << res << "\n";
  }
}

int main()
{
  ios_base::sync_with_stdio(0);
  int t;
  cin>> t;
  RE(i, t)
  {
    solve(i);
  }
  return 0;
}
