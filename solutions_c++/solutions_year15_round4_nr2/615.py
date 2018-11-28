#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>
#pragma comment(linker, "/STACK:266777216")
using namespace std;

#define assert(f) { if(!(f)) { fprintf(stderr,"Assertion failed: "); fprintf(stderr,#f); fprintf(stderr,"\n"); exit(1); } }

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<double> VD;
typedef pair<double,double> PDD;
typedef pair<LL,LL> PLL;

const int inf=1000000000;
const LL INF=LL(inf)*inf;
const double eps=1e-9;
const double PI=2*acos(0.0);
#define bit(n) (1<<(n))
#define bit64(n) ((LL(1))<<(n))
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) (a).begin(),(a).end()
#define fill(ar,val) memset((ar),(val),sizeof (ar))
#define MIN(a,b) {if((a)>(b)) (a)=(b);}
#define MAX(a,b) {if((a)<(b)) (a)=(b);}
#define sqr(x) ((x)*(x))
#define X first
#define Y second

clock_t start=clock();

bool lesspt(const PLL& a, const PLL& b) {
  return a.X*b.Y<a.Y*b.X;
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d: ",++tst);
		fprintf(stderr,"Case #%d:\n",tst);
    if(tst==17)
      tst=tst;
    int n;
    double xx,tmp;
    scanf("%d%lf%lf",&n,&xx,&tmp);
    LL X = xx*1e4+0.5;
    LL Y = X * LL(tmp*1e4+0.5);
    PLL a[111];
    for(int i=0;i<n;i++) {
      double r,c;
      scanf("%lf%lf",&r,&c);
      a[i].X=r*1e4+0.5, a[i].Y=a[i].X*LL(c*1e4+0.5);
    }
    sort(a,a+n,lesspt);
    LL x[222],y[222];
    x[0]=y[0]=0.0;
    for(int i=0;i<n;i++) {
      x[i+1]=x[i]+a[i].X;
      y[i+1]=y[i]+a[i].Y;
    }
    for(int i=n;i<2*n;i++) {
      x[i+1]=x[i]-a[i-n].X;
      y[i+1]=y[i]-a[i-n].Y;
    }
    double res=1e30;
    for(int i=1;i<2*n;i++) {
      LL x1=x[i],y1=y[i];
      if(x1*Y==X*y1) {
        MIN(res, double(X)/x1);
      }
      if(i==2*n-1) break;
      LL x2=x[i+1],y2=y[i+1];
      if(x1*y2==x2*y1) continue;
      if(x1*Y-X*y1 > 0) continue;
      if(X*y2-x2*Y > 0) continue;
      MIN(res, double(x1*Y-X*y1 + X*y2-x2*Y) / (x1*y2-x2*y1));
    }
    if(res>1e25) puts("IMPOSSIBLE"); else
      printf("%.8lf\n",res);
	}
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
