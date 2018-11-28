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

const int N=4;
int a[N][N];
int p[N];
int mark[N];

bool rec(int n, int i) {
  if(i==n) return true;
  bool ok = false;
  for(int j=0;j<n;j++)
    if(a[p[i]][j] && !mark[j]) {
      ok = true;
      mark[j]=1;
      if(!rec(n,i+1)) return false;
      mark[j]=0;
    }
  return ok;
}

bool good(int n,int mask) {
  for(int i=0;i<n;i++) {
    p[i]=i;
    for(int j=0;j<n;j++)
      a[i][j] = (mask & bit(i+n*j))>0;
  }
  do {
    fill(mark,0);
    if(!rec(n,0)) return false;
  } while(next_permutation(p,p+n));
  return true;
}

bool ok[N+1][1<<(N*N)];

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
  int cnt=0;
  for(int n=1;n<=N;n++)
    for(int mask=0;mask<bit(n*n);mask++)
      ok[n][mask] = good(n,mask);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d: ",++tst);
		fprintf(stderr,"Case #%d:\n",tst);
    int n;
    scanf("%d",&n);
    int mask=0;
    for(int i=0;i<n;i++) {
      char s[11];
      scanf("%s",s);
      for(int j=0;j<n;j++)
        if(s[j]=='1') mask += bit(i+n*j);
    }
    int res=11111;
    for(int m=0;m<bit(n*n);m++)
      if((m & mask)==mask && ok[n][m]) {
        int dif=m-mask;
        int cnt=0;
        for(int i=0;i<n*n;i++) if(dif & bit(i)) cnt++;
        MIN(res,cnt);
      }
    printf("%d\n",res);
	}
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
