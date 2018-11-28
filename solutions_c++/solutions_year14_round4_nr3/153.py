#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <math.h>
#include <queue>
#include <list>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <ctime>
using namespace std;

#define ALL(c) (c).begin(),(c).end()
#define IN(x,c) (find(c.begin(),c.end(),x) != (c).end())
#define REP(i,n) for (int i=0;i<(n);i++)
#define FOR(i,a,b) for (int i=(a);i<=(b);i++)
#define FORD(i,a,b) for (int i=(a);i>=(b);i--)
#define INIT(a,v) memset(a,v,sizeof(a))
#define UNIQUE(c) (sort(c.begin(),c.end()), c.resize(distance(c.begin(),unique(c.begin(),c.end()))))
template<class A, class B> A cvt(B x) { stringstream ss; ss<<x; A y; ss>>y; return y; }

typedef pair<int,int> PII;
typedef long long int64;

int dir[4][2]={{0,1},{0,-1},{1,0},{-1,0}};
int w,h,b;
int block[1000][4];

int inf=1e9;
int d[1009],done[1009];

int len[1024][1024];

int calc(int f, int t) {
	int dist=inf;
	REP (x1,2) REP (y1,2) {
		int xf=block[f][x1*2], yf=block[f][1+y1*2];
		if (block[t][0]<=xf && xf<=block[t][2]) {
			dist=min(dist, abs(block[t][1]-yf));
			dist=min(dist, abs(block[t][3]-yf));
		}
		if (block[t][1]<=yf && yf<=block[t][3]) {
			dist=min(dist, abs(block[t][0]-xf));
			dist=min(dist, abs(block[t][2]-xf));
		}
		REP (x2,2) REP (y2,2) {
			int xt=block[t][x2*2], yt=block[t][1+y2*2];
			dist=min(dist, max(abs(xt-xf),abs(yt-yf)));
		}
	}
	return dist;
}

int main() {
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C.out","w",stdout);
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int tests;
	scanf("%d",&tests);
	FOR (test,1,tests) {
		fprintf(stderr,"%d/%d\n",test,tests);
		scanf("%d %d %d",&w,&h,&b);
		REP (i,b) {
			REP (j,4) scanf("%d",&block[i][j]);
		}
		block[b][0]=-1;  block[b][1]=0;   block[b][2]=-1;  block[b][3]=h;
		block[b+1][0]=w; block[b+1][1]=0; block[b+1][2]=w; block[b+1][3]=h;
		REP (i1,b+2) {
			REP (i2,b+2) {
				len[i1][i2]=min(calc(i1,i2),calc(i2,i1));
				//REP (j,4) printf("%d ",block[i1][j]); printf("\n");
				//REP (j,4) printf("%d ",block[i2][j]); printf("\n");
				//printf("%d %d: %d\n",i1,i2,len[i1][i2]);
			}
		}
		INIT(done,0);
		REP (i,b+2) d[i]=inf;
		d[b]=0;
		while (1) {
			// closest
			int c=-1;
			REP (i,b+2) if (!done[i]) {
				if (c==-1 || d[i]<d[c]) c=i;
			}
			if (c==b+1) break;
			done[c]=1;
			// update
			REP (i,b+2) if (!done[i]) {
				d[i]=min(d[i],d[c]+len[c][i]-1);
			}
		}
		printf("Case #%d: %d\n",test,d[b+1]);
	}
	return 0;
}
