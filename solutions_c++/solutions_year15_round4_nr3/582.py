#include <cstdio>
#include <utility>
#include <cmath>
#include <algorithm>
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

void Test(int x,int y,int z) {
	if (!a[x][y]) ++B;
	else if (a[x][y]==z) ++A;
}

bool Check(int x,int y) {
	A=0;
	B=0;
	if (y>1) Test(x,y-1,a[x][y]); else Test(x,m,a[x][y]);
	if (y<m) Test(x,y+1,a[x][y]); else Test(x,1,a[x][y]);
	if (x>1) Test(x-1,y,a[x][y]);
	if (x<n) Test(x+1,y,a[x][y]);
	return (A<=a[x][y])&&(a[x][y]<=A+B);
}

void Dfs(int x,int y) {
	if (y==m+1) {
		dfs(x+1,1);
		return;
	}
	if (x==n+1) {
		return ret;
	}
	REP(i,4) {
		a[x][y]=i;
		bool flag=true;
		if (!Check(x,y)) flag=false;
		if (x>1 && !Check(x,y)) flag=false;
		if (y>1 && !Check(x,y)) flag=false;
		a[x][y]=0;
	}
}

int main() {
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		printf("Case #%d: ",T_T);
		scanf("%d%d",&n,&m);
		Dfs(1,1);
	}
	return 0;
}