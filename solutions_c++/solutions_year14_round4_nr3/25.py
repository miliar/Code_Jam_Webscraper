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

int dist (int l1, int r1, int l2, int r2)
{
  if (r1<=l2)
    return l2-r1;
  if (r2<=l1)
    return l1-r2;
  return 0;
}

int X[1100][4];

int dist (int a, int b)
{
  return max(dist(X[a][0],X[a][2],X[b][0],X[b][2]),dist(X[a][1],X[a][3],X[b][1],X[b][3]));
}

int D[1100][1100], R[1100];
set<pii> S;

void add (int v, int d)
{
  if (R[v]<=d)
    return;
  S.erase(mp(R[v],v)), R[v]=d, S.insert(mp(d,v));
}

void solve (int tst)
{
  cerr<<"solve tst="<<tst<<endl;
  int n, m, b, i, j;
  scanf("%d%d%d", &n, &m, &b);
  for (i=0; i<b; i++)
  {
    for (j=0; j<4; j++)
      scanf("%d", &X[i][j]);
    X[i][2]++, X[i][3]++;
  }
  X[b][0]=0, X[b][1]=0, X[b][2]=0, X[b][3]=m;
  X[b+1][0]=n, X[b+1][1]=0, X[b+1][2]=n, X[b+1][3]=m;
  for (i=0; i<=b+1; i++)
    for (j=i; j<=b+1; j++)
      D[i][j]=dist(i,j), D[j][i]=D[i][j]; 
  /*for (i=0; i<=b+1; i++, cerr<<endl)
    for (j=0; j<=b+1; j++)
      cerr<<D[i][j];  */
  for (i=0; i<=b+1; i++)
    R[i]=inf;
  add(b,0);
  while (S.size())
  {
    int v=S.begin()->second, d=S.begin()->first;
    S.erase(S.begin());
    for (i=0; i<=b+1; i++)
      add(i,d+D[v][i]);
  }
  printf("Case #%d: %d\n", tst, R[b+1]);
}
               
int main()
{
  int tst;
  #ifdef LOCAL
  freopen("C-large.in","r",stdin);
  freopen(TASKNAME"out","w",stdout);
  #endif
  scanf("%d", &tst);
  for (int cnt=1; cnt<=tst; cnt++)
    solve(cnt);  
  TIMESTAMP(end);
  return 0;
}
