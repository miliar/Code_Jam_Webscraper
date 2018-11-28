#include<stdio.h>
long long int insomnia(long long int n){
	long long int insomnia[10], num=0, imsi,first = n;
	for(int i=0;i<10;i++){
		insomnia[i] = 0;
	}
	if(n==0){ return -1;
	}
	else{
		while(num<10){
			for(int i=0;i<10;i++){
				imsi = n;
				while(imsi>0){
					if(imsi%10==i && insomnia[i]==0){
						insomnia[i]=1;
						num++;
					}
					imsi/=10;
				}
			}
			if(num==10){
				return n;
			}
			n+=first;
		}
	}
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("result.txt","w",stdout);
	long long int T,n;
	scanf("%lld",&T);
	for(int i=0;i<T;i++){
		scanf("%lld",&n);
		if(insomnia(n)==-1){
			printf("Case #%lld: INSOMNIA\n",i+1);
		}
		else{
			printf("Case #%d: %lld\n",i+1,insomnia(n));
		}
	}
}
