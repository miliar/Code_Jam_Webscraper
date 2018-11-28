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

#define N 111

int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d: ",++tst);
		fprintf(stderr,"Case #%d:\n",tst);
    int k,n,m;
    char alp[N],s[N];
    scanf("%d%d%d%s%s",&k,&n,&m,alp,s);
    int cnt[26]={0};
    for(int i=0;i<k;i++)
      cnt[alp[i]-'A']++;

    bool exists=true;
    for(int i=0;i<n && exists;i++)
      if(!cnt[s[i]-'A']) exists=false;
    if(!exists) {
      puts("0");
      continue;
    }

    int p;
    for(p=1;p<n;p++) {
      int j;
      for(j=0;p+j<n && s[j]==s[p+j];j++);
      if(p+j==n) break;
    }
    int res1 = (m-n)/p+1;

    int maxpref[N][26];
    for(int x=0;x<=n;x++)
      for(int c=0;c<26;c++) {
        if(s[x]==c+'A') {
          maxpref[x][c]=x+1;
          continue;
        }
        char t = s[x];
        s[x] = c+'A';
        int i;
        for(i=1;i<=x;i++) {
          int j;
          for(j=0;i+j<=x && s[j]==s[i+j];j++);
          if(i+j>x) break;
        }
        maxpref[x][c]=x+1-i;
        s[x] = t;
      }

    double num[N][N]={1},sum[N][N]={0};
    double res=0;
    for(int j=0;j<=m;j++)
      for(int i=0;i<=n;i++) {
        if(j==m) {
          res += sum[j][i];
          continue;
        }
        if(num[j][i]==0) continue;
        for(int c=0;c<26;c++) if(cnt[c]) {
          double prob = double(cnt[c])/k;
          int x=maxpref[i][c];
          num[j+1][x]+=num[j][i]*prob;
          sum[j+1][x]+=(sum[j][i]+(x==n)*num[j][i])*prob;
        }
      }
    printf("%.8lf\n",res1-res);
	}
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
