#include <stdio.h>

#define MAXN 105

char a[MAXN][MAXN];

int n,m;

int _dx[4]={-1,1,0,0};
int _dy[4]={0,0,-1,1};

inline bool check(int x0,int y0)
{
	int x,y;
	int i;
	for (i=0;i<4;i++) {
		int dx=_dx[i],dy=_dy[i];
		x=x0+dx;y=y0+dy;
		while (x>=1 && x<=n && y>=1 && y<=m) {
			if (a[x][y]!='.') break;
			x+=dx;y+=dy;
		}
		if (x>=1 && x<=n && y>=1 && y<=m) {
			return 0;
		}
	}
	return 1;
}

inline void solve()
{
	scanf("%d%d",&n,&m);
	int i,j;
	for (i=1;i<=n;i++) {
		for (j=1;j<=m;j++) {
			char ch=getchar();
			while (ch<=32) ch=getchar();
			a[i][j]=ch;
		}
	}
	int ans=0;
	for (i=1;i<=n;i++) {
		for (j=1;j<=m;j++) {
			if (a[i][j]=='.') continue;
			int dx=0,dy=0;
			if (a[i][j]=='>') dy=1;
			if (a[i][j]=='<') dy=-1;
			if (a[i][j]=='^') dx=-1;
			if (a[i][j]=='v') dx=1;
			int x=i+dx,y=j+dy;
			while (x>=1 && x<=n && y>=1 && y<=m) {
				if (a[x][y]!='.') break;
				x+=dx;y+=dy;
			}
			if (x>=1 && x<=n && y>=1 && y<=m) continue;
			if (check(i,j)) {
				puts("IMPOSSIBLE");
				return;
			} else {
				++ans;
			}
		}
	}
	printf("%d\n",ans);
}

int main()
{
	int T;
	scanf("%d",&T);
	int i;
	for (i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		solve();
	}
}