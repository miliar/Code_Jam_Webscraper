#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
#define maxn 10005
#define mem(a,b) memset(a,b,sizeof(a))
#define mcp(a,b) memcpy(a,b,sizeof(a))
using namespace std;

int T,n,tot,R,P,S;

int f[maxn];

int ans[maxn];

void dfs(int l,int r,int win){
	if (l==r) {
		f[l]=win;
		return;
	}
	int mid=(l+r) >> 1;
	dfs(l,mid,win);
	dfs(mid+1,r,(win-1+3) % 3);
	bool ok=0;
	int l1=l,l2=mid+1;
	while (l1<=mid) {
		if (f[l1]<f[l2]) {
			ok=0;
			break;
		}
		if (f[l1]>f[l2]) {
			ok=1;
			break;
		}
		l1++;
		l2++;
	}
	if (ok) {
		l1=l,l2=mid+1;
		while (l1<=mid) {
			swap(f[l1],f[l2]);
			l1++;
			l2++;
		}
	}
}

int main(){
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d",&T);
	fo(kk,1,T) {
		printf("Case #%d: ",kk);
		scanf("%d%d%d%d",&n,&R,&P,&S);
		tot=1 << n;
		ans[1]=1000;
		////
		fo(win,0,2){
			mem(f,0);
			dfs(1,tot,win);
			int sum[3];
			sum[0]=0;
			sum[1]=0;
			sum[2]=0;
			fo(i,1,tot) sum[f[i]]++;
			if (sum[0]!=P || sum[1]!=R || sum[2]!=S) continue;
			bool ok=0;
			fo(i,1,tot) {
				if (f[i]<ans[i]) {
					ok=1;
					break;
				}
				if (f[i]>ans[i]) {
					ok=0;
					break;
				}
			}
			if (ok) {
				mcp(ans,f);
			}
		}
		if (ans[1]==1000) {
			puts("IMPOSSIBLE");
		}
		else {
			fo(i,1,tot) {
				if (ans[i]==0) putchar('P');
				if (ans[i]==1) putchar('R');
				if (ans[i]==2) putchar('S');
			}
			puts("");
		}
		////
	}
	return 0;
}
