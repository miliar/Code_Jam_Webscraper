#include<cstdio>
int n,a[1010],ans,T;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;++test){
		ans=1000000000;
		scanf("%d",&n);
		for(int i=1;i<=n;++i)scanf("%d",&a[i]);
		for(int i=1;i<=1000;++i){
			int k=i;
			for(int j=1;j<=n;++j)
				k+=(a[j]-1)/i;
			if(k<ans)ans=k;
		}
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
} 
