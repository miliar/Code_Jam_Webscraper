#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <iostream>

#define pb push_back
#define mp make_pair
#define TASKNAME ""

#ifdef LOCAL
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...)
#endif

#define TIMESTAMP(x) eprintf("[" #x "] Time = %.3lfs\n",clock()*1.0/CLOCKS_PER_SEC)

#ifdef linux
#define LLD "%lld"
#else
#define LLD "%I64d"
#endif

#define sz(x) ((int)(x).size())

using namespace std;

typedef long double ld;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;
typedef pair <ll, ll> pll;
typedef vector<pii> vpii;

const int inf = 1e9;
const double eps = 1e-9;
const double INF = inf;
const double EPS = eps;

double A[1100], B[1100];

int solve2 (int n)
{
  int ret=0;
  set<double> S1, S2;
  for (int i=0; i<n; i++)
    S1.insert(A[i]);
  for (int i=0; i<n; i++)
    S2.insert(B[i]);
  while (S1.size())
  {
    if ((*--S2.end())<(*--S1.end()))
      ret++, S1.erase(--S1.end()), S2.erase(S2.begin());
    else
      S2.erase(S2.lower_bound(*--S1.end())), S1.erase(--S1.end());
  }
  return ret;
}

int solve1 (int n)
{
  int ret=0;
  set<double> S1, S2;
  for (int i=0; i<n; i++)
    S1.insert(A[i]);
  for (int i=0; i<n; i++)
    S2.insert(B[i]);
  while (S1.size())
  {
    if ((*--S2.end())<(*--S1.end()))
      ret++, S1.erase(S1.lower_bound(*--S2.end())), S2.erase(--S2.end());
    else
      S1.erase(S1.begin()), S2.erase(--S2.end());
  }
  return ret;
}

void solve (int tst)
{
  int i, n;
  scanf("%d", &n);
  for (i=0; i<n; i++)
    scanf("%lf", &A[i]);
  for (i=0; i<n; i++)
    scanf("%lf", &B[i]);
  sort(A,A+n), sort(B,B+n);
  printf("Case #%d: %d %d\n", tst, solve1(n), solve2(n));
}
               
int main()
{
  int tst;
  #ifdef LOCAL
  freopen(TASKNAME"in","r",stdin);
  freopen(TASKNAME"out","w",stdout);
  #endif
  scanf("%d", &tst);
  for (int cnt=1; cnt<=tst; cnt++)
    solve(cnt);  
  TIMESTAMP(end);
  return 0;
}
