#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>

using namespace std;

int a[10010];
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,n,m,ri=1;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++){
			scanf("%d",&a[i]);
		}
		sort(a,a+n);
		int t=0,ans=0;
		for(int i=n-1;i>=t;i--){
			if(i>t&&a[i]+a[t]<=m){
				t++;
			}
			ans++;
		}
		printf("Case #%d: %d\n",ri++,ans);
	}

	return 0;
}
