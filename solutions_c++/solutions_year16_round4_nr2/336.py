#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
#define maxn 205
#define db double
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;

db p[maxn];

int T,n,k;

int now[maxn];

db ans;

db f[maxn][maxn];

db q[maxn];

void calc(int w){
	int nowtot=0;
	fo(i,1,w) q[++nowtot]=p[i];
	fo(i,n-(k-w)+1,n) q[++nowtot]=p[i];
	mem(f,0);
	f[0][0]=1;
	fo(i,1,k) {
		fo(j,1,k) {
			f[i][j]=f[i-1][j]*(1-q[i])+f[i-1][j-1]*q[i];
		}
		f[i][0]=f[i-1][0]*(1-q[i]);
	}
	ans=max(ans,f[k][k / 2]);
}

int main(){
	freopen("2.in", "r", stdin);
	freopen("bbb.out", "w", stdout);
	scanf("%d",&T);
	fo(kk,1,T) {
		printf("Case #%d: ",kk);
		scanf("%d%d",&n,&k);
		fo(i,1,n) cin>>p[i];
		sort(p+1,p+n+1);
		ans=0;
		fo(i,0,k) calc(i);
		printf("%.10lf\n",ans);
	}
	return 0;
}
