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

int v[205][105][105], idx, n, k;
long double DP[205][105][105];
double p[205];
bool taken[205];

long double solve(int ind, int pos, int neg)
{
  if(pos < 0 || neg < 0) return 0;
  if(ind == n) return pos == 0 && neg == 0;
  long double &temp = DP[ind][pos][neg];
  if(v[ind][pos][neg] == idx) return temp;
  v[ind][pos][neg] = idx;
  if(!taken[ind]) return temp = solve(ind + 1, pos, neg);
  // take
  temp = solve(ind + 1, pos - 1, neg) * p[ind] + solve(ind + 1, pos, neg - 1) * (1 - p[ind]);
  return temp;
}
long double res;
void stupid(int ind, int ch)
{
  if(ind == n && !ch)
  {
    idx++;
    res = max(res, solve(0, k/2, k/2));
    /*if(res == 0.5)
    {
      for(int i=0;i<n;i++)
        cout << taken[i] << " ";
      cout << "\n";
    }*/
    return;
  }
  if(ind == n) return;
  if(ch)
  {
    taken[ind] = true;
    stupid(ind + 1, ch - 1);
    taken[ind] = false;
  }
  stupid(ind + 1, ch);
}

int main()
{
  freopen("B-small-attempt0.in", "r", stdin);
  freopen("output.out", "w", stdout);
  int t, tt = 1;
  cin >> t;
  while(t--)
  {
    cin >> n >> k;
    for(int i=0;i<n;i++)
      scanf("%lf", &p[i]);
    idx++;
    res = 0;
    setzero(taken);
    stupid(0, k);
    printf("Case #%d: %.15lf\n", tt++, (double)res);
    /*res = 0;
    for(int it=0;it<k;it+=2)
    {
      double tmp = -1;
      pair<int, int> ch;
      for(int i=0;i<n;i++)
      {
        if(taken[i]) continue;
        for(int j=0;j<n;j++)
        {
          if(taken[j] || i == j) continue;
          idx++;
          double x = (p[i] * (1 - p[j]) + p[j] * (1 - p[i])) * solve(0, it/2, it/2);
          x += p[i] * p[j] * solve(0, it/2 - 1, it/2 + 1);
          x += (1-p[i]) * (1-p[j]) * solve(0, it/2 + 1, it/2 - 1);
          if(x > tmp)
          {
            tmp = x;
            ch = mp(i, j);
          }
        }
      }
      taken[ch.f] = true;
      taken[ch.s] = true;
    }
    for(int i=0;i<n;i++)
        cout << taken[i] << " ";
      cout << "\n";
    idx++;
    printf("Case #%d: %.15lf\n", tt++, (double)solve(0, k/2,k/2));*/
  }
  return 0;
}
