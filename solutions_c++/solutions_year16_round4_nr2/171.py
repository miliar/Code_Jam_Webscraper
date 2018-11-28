// Jakub Radoszewski

//#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include<numeric>
#include<cassert>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define INFTY 100000000
#define VAR(V,init) __typeof(init) V=(init)
#define FORE(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define SIZE(x) ((int)(x).size())

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

ll nwd(ll a,ll b) { return !b?a:nwd(b,a%b); }
inline int CEIL(int a,int b) { return a%b ? a/b+1 : a/b; }
template <class T> inline T sqr(const T&a) { return a*a; }

int los(int m)
{
  return (int)((double)m*(rand()/(RAND_MAX+1.0)));
}

int n,k;

double doit(vector<double> A)
{
  double tab[300][300];
  assert(SIZE(A)==k);
  REP(i,n+1) REP(j,n+1) tab[i][j]=0;
  tab[0][0]=1;
  REP(i,k)
  {
    REP(j,k+1)
    {
      tab[i+1][j+1]+=A[i]*tab[i][j];
      tab[i+1][j]+=(1-A[i])*tab[i][j];
    }
  }
  return tab[k][k/2];
}

double t[300];


void mymain()
{
  scanf("%d%d",&n,&k);
  REP(i,n) scanf("%lf",&t[i]);
  sort(t,t+n);
  double p=0;
  FOR(i,0,k)
  {
    vector<double> A;
    REP(a,i) A.PB(t[a]);
    REP(b,k-i) A.PB(t[n-1-b]);
    p=max(p,doit(A));
  }
  printf("%.7lf\n",p);
}

int main()
{
  int ILE;
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d: ",iii);
    fprintf(stderr,"Case #%d:\n",iii);
    mymain();
  }
  return 0;
}
