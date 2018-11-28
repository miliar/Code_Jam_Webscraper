#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <ctime>
#define fi first
#define se second
#define PA pair<int,int>
#define VI vector<int>
#define VP vector<PA >
#define mk(x,y) make_pair(x,y)
#define N 110
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
struct ww {
	int mi,ma;
	void clear() {
		mi=N,ma=0;
	}
	void get(int x) {
		mi=min(mi,x);
		ma=max(ma,x);
	}
} a[N],b[N];
int i,j,k,n,m,te,T,s;
char p[N][N];
int main() {
	freopen("peg.in","r",stdin);
	freopen("peg.out","w",stdout);
	scanf("%d",&T);
	For(te,1,T) {
		scanf("%d%d",&n,&m);
		For(i,1,n) scanf("%s",p[i]+1);
		For(i,0,N-1) a[i].clear(),b[i].clear();
		For(i,1,n)For(j,1,m) if (p[i][j]!='.') {
			a[i].get(j);
			b[j].get(i);
		}
		printf("Case #%d: ",te);
		s=0;
		For(i,1,n)For(j,1,m) if (p[i][j]!='.') {
			if (a[i].mi==j&&a[i].ma==j&&b[j].mi==i&&b[j].ma==i) {
				printf("IMPOSSIBLE\n");
				goto fail;
			}
			int v=1;
			if (p[i][j]=='^'&&b[j].mi<i) v=0;
			if (p[i][j]=='v'&&b[j].ma>i) v=0;
			if (p[i][j]=='<'&&a[i].mi<j) v=0;
			if (p[i][j]=='>'&&a[i].ma>j) v=0;
			s+=v;
		}
		printf("%d\n",s);
		fail:;
	}
	return 0;
}
