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
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
  map<char, PII> dirs;
  dirs['^']=mp(-1,0);
  dirs['v']=mp(1,0);
  dirs['>']=mp(0,1);
  dirs['<']=mp(0,-1);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d: ",++tst);
		fprintf(stderr,"Case #%d:\n",tst);
    int n,m;
    scanf("%d%d",&n,&m);
    char a[111][111];
    for(int i=0;i<n;i++)
      scanf("%s",a[i]);
    int res=0;
    for(int i=0;i<n && res>=0;i++) {
      for(int j=0;j<m && res>=0;j++) {
        if(a[i][j]=='.') continue;
        int id=-1;
        int good[4]={0};
        for(int k=0;k<4;k++) {
          char c = "<>^v"[k];
          if(c==a[i][j]) id=k;
          PII dir = dirs[c];
          int dx=dir.X, dy=dir.Y;
          for(int x=i+dx,y=j+dy;0<=x && x<n && 0<=y && y<m;x+=dx,y+=dy) {
            if(a[x][y]!='.') {
              good[k]=1;
              break;
            }
          }
        }
        if(good[id]) continue;
        res++;
        int k;
        for(k=0;k<4 && !good[k];k++);
        if(k==4) res=-1;
      }
    }
    if(res<0) puts("IMPOSSIBLE"); else printf("%d\n",res);
	}
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
