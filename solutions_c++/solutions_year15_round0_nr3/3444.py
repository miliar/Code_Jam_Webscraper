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

int MULT[5][5]={
  {0,0,0,0,0},
  {0,1,2,3,4},
  {0,2,1,4,3},
  {0,3,4,1,2},
  {0,4,3,2,1}
};

int sign[5][5]={
  {0,0,0,0,0},
  {0,1,1,1,1},
  {0,1,-1,1,-1},
  {0,1,-1,-1,1},
  {0,1,1,-1,-1},
};

int mult(int i, int j) {
  int I=abs(i), J=abs(j);
  return (i*j<0?-1:1) * sign[I][J] * MULT[I][J];
}

#define N 10101

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
    int ind[128]={0};
    ind['i']=2;
    ind['j']=3;
    ind['k']=4;
		printf("Case #%d: ",++tst);
		fprintf(stderr,"Case #%d:\n",tst);
    int l,m,i,j;
    char s[N];
    scanf("%d%d%s",&l,&m,s);
    int a[N];
    int pref[N];
    int suf[N];
    int n=l*m;
    for(i=0;i<n;i++) {
      a[i] = ind[s[i%l]];
      pref[i] = i ? mult(pref[i-1], a[i]) : a[i];
    }
    for(i=n-1;i>=0;i--) {
      suf[i] = i == n-1 ? a[i] : mult(a[i], suf[i+1]);
    }
    if(pref[n-1]!=-1) {
      puts("NO");
      continue;
    }
    for(i=0;i<n && pref[i]!=2;i++);
    for(j=n-1;j>=0 && suf[j]!=4;j--);
    puts(i<j?"YES":"NO");
  }
  fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
