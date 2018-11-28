#include<cstdio>
#include<algorithm>
using namespace std;
int a[20000];
void work(int te){
	printf("Case #%d: ",te);
	int n,s;
	scanf("%d%d",&n,&s);
	for(int i=1;i<=n;++i)scanf("%d",&a[i]);
	sort(a+1,a+n+1);
	int ans=0;
	int l=1,r=n;
	while(l<=r){
		++ans;
		if(a[l]+a[r]<=s){
			l++;r--;
		}else r--;
	}
	printf("%d\n",ans);
	
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tt;
	scanf("%d",&tt);
	for(int i=1;i<=tt;++i)work(i);
	return 0;
} 
