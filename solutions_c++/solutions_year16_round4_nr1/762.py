#include <bits/stdc++.h>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 9223372036854775807LL
#define INF 1000000000
#define EPS 1e-8
#define LL long long
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define setzero(a) memset(a,0,sizeof(a))
#define setdp(a) memset(a,-1,sizeof(a))
#define bits(a) __builtin_popcount(a)

using namespace std;

int r, p, s;

// p -> r -> s

string solve(char c, int n)
{
  if(n == 0)
  {
    string res = "";
    res += c;
    return res;
  }
  string s1 = "", s2 = "";
  if(c == 'R')
  {
    s1 = solve('R', n - 1);
    s2 = solve('S', n - 1);
    if(s1 > s2) swap(s1, s2);
    return s1 + s2;
  }
  else if(c == 'S')
  {
    s1 = solve('P', n - 1);
    s2 = solve('S', n - 1);
    if(s1 > s2) swap(s1, s2);
    return s1 + s2;
  }
  else
  {
    s1 = solve('P', n - 1);
    s2 = solve('R', n - 1);
    if(s1 > s2) swap(s1, s2);
    return s1 + s2;
  }
  return "";
}

bool check(string &str)
{
  int rr = r, pp = p, ss = s;
  for(int i=0;i<str.size();i++)
  {
    if(str[i] == 'R') rr--;
    else if(str[i] == 'P') pp--;
    else ss--;
  }
  return rr == 0 && pp == 0 && ss == 0;
}

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("output.out", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    int n;
    cin >> n >> r >> p >> s;
    printf("Case #%d: ", tt++);
    string str;
    str = solve('R', n);
    if(check(str))
    {
      printf("%s\n", str.c_str());
      continue;
    }
    str = solve('P', n);
    if(check(str))
    {
      printf("%s\n", str.c_str());
      continue;
    }
    str = solve('S', n);
    if(check(str))
    {
      printf("%s\n", str.c_str());
      continue;
    }
    printf("IMPOSSIBLE\n");
  }
  return 0;
}
