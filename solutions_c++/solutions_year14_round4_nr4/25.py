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

const int mod = inf+7;

int e, Next[110*1100][26], Cnt[110*1100], T[110*1100];
char s[110];

void addv ()
{
  memset(Next[e],-1,sizeof(Next[e])), Cnt[e]=0, e++;
}

//int D[1100][110];
int D[110], ND[110];
int C[110][110];
int F[110];

inline int mmul (int a, int b)
{
  return (a*1ll*b)%mod;
}

void add (int t, int tv)
{
  int j, k;
  memset(ND,0,sizeof(ND[0])*(tv+1));
  for (j=0; j<=tv; j++)
    for (k=0; k<=t && k<=j; k++)
      if (j+t-k<=tv)
      {
        ND[j+t-k]+=mmul(mmul(D[j],C[j+t-k][j]),C[j][k]);
        ND[j+t-k]%=mod;
      }
  memcpy(D,ND,sizeof(D[0])*(tv+1));
}

void solve (int tst)
{
  cerr<<"tst="<<tst<<endl;
  int n, m, i, j;
  e=0, addv();
  scanf("%d%d", &m, &n);
  /*memset(D,0,sizeof(D));
  D[0][0]=1;
  for (i=0; i<m; i++)
    for (j=0; j<=n; j++)
    {
      D[i+1][j]+=(D[i][j]*1ll*j)%mod, D[i+1][j]%=mod;
      D[i+1][j+1]+=(D[i][j]*1ll*(n-j))%mod, D[i+1][j+1]%=mod;
    } */
  for (i=0; i<m; i++)
  {
    scanf("%s", s);
    int v=0, len=strlen(s);
    for (j=0; j<len; Cnt[v]++, v=Next[v][s[j]-'A'], j++)
      if (Next[v][s[j]-'A']==-1)
        Next[v][s[j]-'A']=e, addv();
    Cnt[v]++;
  }
  int res=0, cnt=1;
  for (int v=e-1; v>=0; v--)
  {
    T[v]=min(n,Cnt[v]);
    res+=T[v];
    for (i=0; i<=T[v]; i++)
      D[i]=0;
    D[0]=1;
    bool fl=1;
    int ls=Cnt[v];
    for (i=0; i<26; i++)
      if (Next[v][i]!=-1)
      {
        fl=0;
        int t=T[Next[v][i]];
        ls-=Cnt[Next[v][i]];
        add(t,T[v]);
        //cerr<<"???   "<<v<<"    "<<Next[v][i]<<endl;
      }
    if (fl)
      D[T[v]]=1;
    else
      add(ls,T[v]);
    //cerr<<v<<" "<<T[v]<<" "<<Cnt[v]<<"    "<<D[T[v]]<<endl;
    if (n<=4 && m<=8)
      assert(D[T[v]]);
    cnt=(cnt*1ll*D[T[v]])%mod;
  }
  printf("Case #%d: %d %d\n", tst, res, cnt);
}
               
int main()
{
  int tst, i, j;
  #ifdef LOCAL
  freopen(TASKNAME"D-large.in","r",stdin);
  freopen(TASKNAME"outL","w",stdout);
  #endif
  for (i=0; i<110; i++)
    for (C[i][0]=1, j=1; j<=i; j++)
      C[i][j]=(C[i-1][j-1]+C[i-1][j])%mod;
  for (F[0]=1, i=1; i<110; i++)
    F[i]=mmul(F[i-1],i);
  scanf("%d", &tst);
  for (int cnt=1; cnt<=tst; cnt++)
    solve(cnt);  
  TIMESTAMP(end);
  return 0;
}
