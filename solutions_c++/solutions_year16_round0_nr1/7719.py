#include <stdio.h>

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	long long int n;
	for(int i=1;i<=t;i++){
		int ans[12]={0};
		//for(int j=0;j<=9;j++) ans[j]=0;
		scanf("%lld",&n);
		int kali=1;
		int loop=n;
		long long int jawab;
		if(n!=0){
			for(;;kali++){
				jawab = n;
				for(;;){
					if(n<=9){
						ans[n]=1;
						break;
					}
					else{
						ans[n%10]=1;
						n/=10;
					}
				}
				int flag=1;
				for(int j=0;j<=9;j++) if(ans[j]==0) flag=0;
				if(flag==1) break;
				n=loop*kali;
			}
		}
		if(n!=0)printf("Case #%d: %lld\n",i,jawab);
		else printf("Case #%d: INSOMNIA\n",i);
	}
	
	return 0;
}
