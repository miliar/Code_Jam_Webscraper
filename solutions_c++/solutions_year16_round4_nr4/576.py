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

char s[5][5];
int n;

int ans;

void stupid(int x, int y, int cnt = 0)
{
  if(cnt >= ans) return;
  if(x == n)
  {
    int a[] = {0, 1, 2, 3};
    int b[] = {0, 1, 2, 3};
    for(int it=0;it<200;it++)
    {
      int mask = 0;
      random_shuffle(a, a + n);
      for(int i=0;i<n;i++)
      {
        random_shuffle(b, b + n);
        for(int j=0;j<n;j++)
        {
          if(s[a[i]][b[j]] == '0') continue;
          if((mask & (1 << b[j])) == 0)
          {
            mask |= (1 << b[j]);
            break;
          }
        }
        if(bits(mask) != i + 1)
          return;
      }
    }
    ans = cnt;
    return;
  }
  if(y == n)
  {
    stupid(x + 1, 0, cnt);
    return;
  }
  stupid(x, y + 1, cnt);
  if(s[x][y] == '0')
  {
    s[x][y] = '1';
    stupid(x, y + 1, cnt + 1);
    s[x][y] = '0';
  }
}

int main()
{
  freopen("D-small-attempt0.in", "r", stdin);
  freopen("res.out", "w", stdout);
  srand(time(0));
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    cin >> n;
    for(int i=0;i<n;i++)
      scanf("%s", s[i]);
    ans = INF;
    stupid(0, 0);
    printf("Case #%d: %d\n", tt++, ans);
  }
  return 0;
}
