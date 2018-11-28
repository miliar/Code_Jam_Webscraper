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

int main()
{
  const int N = 14;
  string a[N][3];
  char ch[4]="PRS";
  int id[128]={0};
  for(int c=0;c<3;c++) {
    a[0][c] = string(1, ch[c]);
    id[ch[c]]=c;
  }
  for(int n=1;n<N;n++)
    for(int c=0;c<3;c++) {
      int d=(c+1)%3;
      a[n][c] = min(a[n-1][c] + a[n-1][d], a[n-1][d] + a[n-1][c]);
    }
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d: ",++tst);
		fprintf(stderr,"Case #%d:\n",tst);
    int n,r,p,s;
    scanf("%d%d%d%d",&n,&r,&p,&s);
    bool possible=false;
    for(int c=0;c<3;c++) {
      int cnt[3]={0};
      for(int i=0;i<a[n][c].size();i++)
        cnt[id[a[n][c][i]]]++;
      if(cnt[0]==p && cnt[1]==r && cnt[2]==s) {
        possible=true;
        puts(a[n][c].c_str());
      }
    }
    if(!possible) puts("IMPOSSIBLE");
	}
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
