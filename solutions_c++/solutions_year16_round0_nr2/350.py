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

const int maxN = 15;
int bfs[1<<maxN];
int d[1<<maxN];
int gr[1<<maxN];

int naive(int x) {
  if(x==0) return 0;
  if(gr[x]) return gr[x];
  int n;
  for(n=1;;n++)
    if(x<bit(n)) break;
  int& res = gr[x];
  int a[maxN];
  for(int i=0;i<n;i++) a[i] = (x>>i)%2;
  for(int i=0,j;i<n;i=j) {
    for(j=i;j<n && a[i]==a[j];j++);
    res++;
  }
  return res;
}

void research(int n) {
  int N=1<<n;
  int len=0;
  bfs[len++]=0;
  d[0]=0;
  for(int x=1;x<N;x++) d[x]=-1;
  for(int k=0;k<len;k++) {
    int x=bfs[k];
    int a[maxN];
    for(int i=0;i<n;i++) a[i] = (x>>i)%2;
    for(int j=0;j<n;j++) {
      int y=0;
      for(int i=0;i<=j;i++) y += (!a[j-i])<<i;
      for(int i=j+1;i<n;i++) y += a[i]<<i;
      if(d[y]<0) {
        d[y]=d[x]+1;
        bfs[len++]=y;
      }
    }
  }
  for(int x=0;x<N;x++) {
    int naiv = naive(x);
    if(d[x]==naiv) continue;
    for(int i=0;i<n;i++)
      printf("%d",(x>>i)%2);
    printf(" %d %d\n",d[x],naiv);
  }
}

int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d: ",++tst);
		fprintf(stderr,"Case #%d:\n",tst);
    char s[111];
    scanf("%s",s);
    int n=strlen(s);
    for(;n>0 && s[n-1]=='+';n--);
    int res=0;
    for(int i=0,j;i<n;i=j) {
      for(j=i;j<n && s[i]==s[j];j++);
      res++;
    }
    printf("%d\n",res);
	}
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
