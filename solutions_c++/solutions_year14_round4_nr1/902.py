#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int tests,cc,ans,i,j,k,n,m,a[110001];
int main(){
	scanf("%d",&tests);
	for (cc=1;cc<=tests;cc++){
		scanf("%d%d",&n,&m);
		for (i=1;i<=n;i++) scanf("%d",&a[i]);
		sort(a+1,a+1+n);
		for (i=n,ans=0,j=1;i>=j;i--){
			if (a[i]+a[j]<=m) j++;
			ans++;
		}
		printf("Case #%d: %d\n",cc,ans);
	}
	return 0;
}
