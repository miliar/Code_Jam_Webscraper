#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
#define maxn 15
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;

int a[maxn][maxn];

int T,n;

int ans;

int f[maxn];

bool bz[maxn];

bool dfs1(int w,int S){
	if (w==n+1) return 1;
	fo(i,1,n) {
		if (((1<<(i-1))&S)==0) {
			bool ok=0;
			fo(j,1,n) {
				if (a[i][j]==0 || bz[j]) continue;
				bz[j]=1;
				ok=1;
				if (!dfs1(w+1,S|(1<<(i-1)))) return 0;
				bz[j]=0;
			}
			if (ok==0) return 0;
		}
	}
	return 1;
}

bool pd(){
	mem(bz,0);
	return dfs1(1,0);
}

void dfs(int x,int y,int tot){
	if (tot>=ans) return;
	if (x==n+1) {
		if (pd()) ans=tot;
		return; 
	}
	if (y==n+1) {
		dfs(x+1,1,tot);
		return;
	}
	if (a[x][y]) {
		dfs(x,y+1,tot);
		return;
	}
	dfs(x,y+1,tot);
	a[x][y]=1;
	dfs(x,y+1,tot+1);
	a[x][y]=0;
}

int main(){
	freopen("4.in","r",stdin);
	freopen("4.out","w",stdout);
	scanf("%d",&T);
	fo(kk,1,T) {
		printf("Case #%d: ",kk);
		scanf("%d",&n);
		fo(i,1,n)
			fo(j,1,n) {
				char c=getchar();
				while (c!='0' && c!='1') c=getchar();
				a[i][j]=c-'0';
			}
		ans=n*n;
		dfs(1,1,0);
		cout<<ans<<endl;
	}
	return 0;
}
