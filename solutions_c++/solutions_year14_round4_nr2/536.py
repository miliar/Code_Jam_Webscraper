#include<cstdio>
#include<algorithm>
using namespace std;
int a[1010],b[1010],n;

void work(int te){
	printf("Case #%d: ",te);
	scanf("%d",&n);
	int ans=0;
	for(int i=1;i<=n;++i)scanf("%d",&a[i]);
	int l=1,r=n;
	for(int i=1;i<n;++i){
		int mi=1100000000,p=-1;
		for(int j=l;j<=r;++j)
			if(a[j]<mi){
				mi=a[j];
				p=j;
			}
		if(p-l<r-p){
			ans+=p-l;
			for(int j=p;j>l;--j)swap(a[j],a[j-1]);
			++l;
		}else{
			ans+=r-p;
			for(int j=p;j<r;++j)swap(a[j],a[j+1]);
			--r;
		}
	}
	printf("%d\n",ans);
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int tt;
	scanf("%d",&tt);
	for(int i=1;i<=tt;++i)work(i);
	return 0;
} 
