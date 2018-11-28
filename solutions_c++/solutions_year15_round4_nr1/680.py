#include <cstdio>
#include <cstring>

using namespace std;
#define rep(i,l,r) for (int i=(l);i<=(r);i++)
#define repd(i,r,l) for (int i=(r);i>=(l);i--)
const int maxn=150;
char a[maxn][maxn];
int n,m;

bool pd(int x,int y) {
	bool can=false;
	rep(i,1,n)
		if (i!=x&&a[i][y]!='.')
		{can=true;break;}
	if (!can)
	rep(j,1,m)
		if (j!=y&&a[x][j]!='.')
		{can=true;break;}
	return can;
}

int chk(int x,int y) {
	if (a[x][y]=='^') {
		bool ff=false;
		repd(i,x-1,1)
			if (a[i][y]!='.') {ff=true;break;}
		if (!ff) {
			if (!pd(x,y)) return -1;
			else return 1;
		}
	}
	if (a[x][y]=='v') {
		bool ff=false;
		rep(i,x+1,n)
			if (a[i][y]!='.') {ff=true;break;}
		if (!ff) {
			if (!pd(x,y)) return -1;
			else return 1;
		}
	}
	if (a[x][y]=='<') {
		bool ff=false;
		repd(i,y-1,1)
			if (a[x][i]!='.') {ff=true;break;}
		if (!ff) {
			if (!pd(x,y)) return -1;
			else return 1;
		}
	}
	if (a[x][y]=='>') {
		bool ff=false;
		rep(i,y+1,m)
			if (a[x][i]!='.') {ff=true;break;}
		if (!ff) {
			if (!pd(x,y)) return -1;
			else return 1;
		}
	}
	/*
	if (x==1&&a[x][y]=='^') {
		if (!pd(x,y)) return -1;
		else return 1;
	}
	if (x==n&&a[x][y]=='v') {
		if (!pd(x,y)) return -1;
		else return 1;
	}
	if (y==1&&a[x][y]=='<') {
		if (!pd(x,y)) return -1;
		else return 1;
	}
	if (y==m&&a[x][y]=='>') {
		if (!pd(x,y)) return -1;
		else return 1;
	}
	*/
	return 0;
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;scanf("%d\n",&T);
	rep(t,1,T) {
		printf("Case #%d: ",t);
		scanf("%d%d\n",&n,&m);
		rep(i,1,n) {
			scanf("%s\n",a[i]+1);
		}
		int ans=0;
		bool flag=true;
		rep(i,1,n) {
			rep(j,1,m) if (a[i][j]!='.') {
				int p=chk(i,j);
				if (p==-1)
					flag=false;
				else ans+=p;
				if (!flag) break;
			}
			if (!flag) break;
		}
		if (!flag) {
			puts("IMPOSSIBLE");
			continue;
		}
		printf("%d\n",ans);
	}
	return 0;
}
