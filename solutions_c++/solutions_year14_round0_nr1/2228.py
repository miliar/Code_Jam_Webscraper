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

int R[2], A[20][2];

void solve (int tst)
{
  int i, j, it, v;
  printf("Case #%d: ", tst);
  for (it=0; it<2; it++)
    for (scanf("%d", &R[it]), i=0; i<4; i++)
      for (j=0; j<4; j++)
        scanf("%d", &v), A[v][it]=i+1;
  vi V;
  for (i=1; i<=16; i++)
    if (R[0]==A[i][0] && R[1]==A[i][1])
      V.pb(i);
  if (!V.size())
  {
    puts("Volunteer cheated!");
    return;
  }
  if ((int)V.size()>1)
  {
    puts("Bad magician!");
    return;
  }
  printf("%d\n", V[0]);
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
