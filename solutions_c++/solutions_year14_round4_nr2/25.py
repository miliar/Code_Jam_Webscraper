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

int A[1100], B[1100], P[1100];

void solve (int tst)
{
  int i, n, j, res=0;
  scanf("%d", &n);
  for (i=0; i<n; i++)
    scanf("%d", &A[i]), B[i]=A[i];
  sort(B,B+n);
  for (i=0; i<n; i++)
    A[i]=lower_bound(B,B+n,A[i])-B, P[A[i]]=i;
  for (i=0; i<n; i++)
  {
    int t=0;
    for (j=i+1; j<n; j++)
      if (P[j]<P[i])
        t++;
    assert(t<=n-1-i);
    res+=min(t,n-1-i-t);
  }
  printf("Case #%d: %d\n", tst, res);
}
               
int main()
{
  int tst;
  #ifdef LOCAL
  freopen(TASKNAME"B-large.in","r",stdin);
  freopen(TASKNAME"outL","w",stdout);
  #endif
  scanf("%d", &tst);
  for (int cnt=1; cnt<=tst; cnt++)
    solve(cnt);  
  TIMESTAMP(end);
  return 0;
}
