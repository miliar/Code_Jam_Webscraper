#include<cstdio>
#include<cstring>
#include<algorithm>
int n,a[1024],ans,l,r,T,TT,i,j;
using namespace std;
int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&TT);
	for(T=1;T<=TT;T++){
		scanf("%d",&n);
		for(i=1;i<=n;i++)scanf("%d",&a[i]);
		ans=0;
		for(i=1;i<=n;i++){
			l=r=0;
			for(j=1;j<i;j++)if(a[j]>a[i])l++;
			for(j=i+1;j<=n;j++)if(a[j]>a[i])++r;
			ans+=min(l,r);
		}
		printf("Case #%d: %d\n",T,ans);
	}
}