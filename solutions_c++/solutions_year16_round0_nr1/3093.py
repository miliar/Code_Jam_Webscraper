#include <cstdio>
#define LL long long
int T;
int a[10];
int main(){
	scanf("%d",&T);
	for (int Case=1;Case<=T;Case++){
		for (int i=0;i<10;i++)a[i]=0;	
		LL n;
		bool ans=false;
		LL value;
		scanf("%lld",&n);
		if (n==0LL){
			printf("Case #%d: INSOMNIA\n",Case);
		}
		else {
			for (LL i=n;ans==false;i+=n){
				ans=true;
				LL x = i;
				value=i;
				while (x!=0){
					a[x%10]=1;
					x/=10;
				}
				for (int i=0;i<10;i++)if (a[i]==0)ans=false;
			}
			printf("Case #%d: %lld\n",Case, value);
		}
	}
	return 0;
}
