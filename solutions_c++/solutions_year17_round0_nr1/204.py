#include <bits/stdc++.h>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 2000000000000000000LL
#define INF 1000000000
#define EPS 1e-7
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

char s[1005];

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    int k;
    scanf("%s %d", s, &k);
    int n = strlen(s);
    bool bad = false;
    int ans = 0;
    for(int i=0;i<n;i++)
    {
      if(s[i] == '+') continue;
      if(i + k > n)
      {
        bad = true;
        break;
      }
      ans++;
      for(int j=i;j<i+k;j++)
      {
        if(s[j] == '+') s[j] = '-';
        else s[j] = '+';
      }
    }
    printf("Case #%d: ", tt++);
    if(bad) printf("IMPOSSIBLE\n");
    else printf("%d\n", ans);
  }
  return 0;
}
