#include <stdio.h>
#include <map>

int n,m;

int a[10][10];
int cnt[10][10];

int ans;

std::map<int,int> M;

#define mo 998244353

inline void update_ans()
{
	int i,j,k;
	int tmp=mo-1;
	for (k=0;k<m;k++) {
		int t=0;
		for (i=1;i<=n;i++) {
			for (j=1;j<=m;j++) {
				int j1=j+k;
				if (j1>m) j1-=m;
				t=(1LL*t*233+a[i][j1])%mo;
			}
		}
		if (t<tmp) tmp=t;
	}
	if (!M[tmp]) {
		M[tmp]=1;
		++ans;
	}
}

inline void dfs(int x,int y)
{
	if (x>n) {
		update_ans();
		return;
	}
	int nx=x,ny=y+1;
	if (ny>m) ny=1,++nx;
	
	int i;
	for (i=1;i<=4;i++) {
		cnt[x][y]=0;
		a[x][y]=i;
		bool fl=0;
		if (x>1) {
			if (a[x-1][y]==i) {
				++cnt[x][y];
				++cnt[x-1][y];
			}
			fl|=cnt[x-1][y]!=a[x-1][y];
		}
		if (y>1) {
			if (a[x][y-1]==i) {
				++cnt[x][y];
				++cnt[x][y-1];
			}
			fl|=cnt[x][y-1]>a[x][y-1];
			if (x==n && y>2) fl|=cnt[x][y-1]!=a[x][y-1];
		}
		if (y==m) {
			if (a[x][1]==i) {
				++cnt[x][y];
				++cnt[x][1];
			}
			fl|=cnt[x][1]>a[x][1];
		}
		fl|=cnt[x][y]>i;
		if (nx>n) fl|=cnt[x][y]!=i,fl|=cnt[x][1]!=a[x][1];
		if (!fl) {
			dfs(nx,ny);
		}
		if (x>1) {
			if (a[x-1][y]==i) {
				--cnt[x-1][y];
			}
		}
		if (y>1) {
			if (a[x][y-1]==i) {
				--cnt[x][y-1];
			}
		}
		if (y==m) {
			if (a[x][1]==i) {
				--cnt[x][1];
			}
		}
	}
}

inline void solve()
{
	scanf("%d%d",&n,&m);
	ans=0;
	M.clear();
	dfs(1,1);
	printf("%d\n",ans);
}

int main()
{
	int T;
	scanf("%d\n",&T);
	int i;
	for (i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		solve();
	}
}