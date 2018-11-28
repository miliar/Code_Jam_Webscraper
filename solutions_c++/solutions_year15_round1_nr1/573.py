#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<iostream>
using namespace std;
__int64 a[1005];
__int64 ans1,ans2,vmax;
int main(){
	freopen("E:A-large.in","r",stdin);
	freopen("E:A-large.out","w",stdout);
	int i,j,n,m,T,vcase=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		for(i=1;i<=n;i++){
			scanf("%I64d",&a[i]);
		}
		vmax=0;ans1=0;ans2=0;
		for(i=1;i<=n;i++){
			if(a[i]<a[i-1]) ans1+=a[i-1]-a[i];
			vmax=max(vmax,a[i-1]-a[i]);
		}
		for(i=1;i<n;i++){
			ans2+=min(vmax,a[i]);
		}
		printf("Case #%d: %I64d %I64d\n",++vcase,ans1,ans2);
	}
	return 0;
}