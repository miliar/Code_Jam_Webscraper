#include <cstdio>
#include <cstring>
bool num[10];
bool ok(){
	bool k=1;
	for(int i=0;i<10;i++)
		k&=num[i];
	return k;
}
int main(){
	freopen("/Users/shintaku/Desktop/A-large.in","r",stdin);
    freopen("/Users/shintaku/Desktop/A-large.out","w",stdout);
	int t,cas=0,n;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		if(n==0)
			printf("Case #%d: INSOMNIA\n",++cas);
		else{
			long long ans=0;
			memset(num,0,sizeof(num));
			while(!ok()){
				ans+=n;
				long long m=ans;
				while(m){
					num[m%10]|=1;
					m/=10;
				}
			}
			printf("Case #%d: %lld\n",++cas,ans);
		}
	}
}