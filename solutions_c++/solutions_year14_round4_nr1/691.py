#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int a[10010];
int vis[10010];
int n,m,ans;
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int ca,cc=0;
	int i,j;
	scanf("%d",&ca);
	while (ca--){
		scanf("%d%d",&n,&m);
		for (i=0;i<n;i++) scanf("%d",&a[i]);
		sort(a,a+n);
		memset(vis,0,sizeof(vis));
		ans=0;
		for (i=0;i<n;i++){
			if (vis[i]) continue;
			vis[i]=1;
			for (j=n-1;j>i;j--){
				if (a[i]+a[j]<=m && !vis[j]) break;
			}
			ans++;
			if (!vis[j]) vis[j]=1;
		}
		printf("Case #%d: %d\n",++cc,ans);
	}
	return 0;
}		
