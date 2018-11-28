#include<stdio.h>
int main(){
	long long int T,N,a,n,Z,cicle,i;
	scanf("%lld",&T);
	for(a=1;a<=T;a++){
		scanf("%lld",&N);
		if(N==0){
			printf("Case #%lld: INSOMNIA\n",a);
		}
		else 
		{
			bool array[10]={false};
			Z=1;
			cicle=1;
			while(Z){
				n=N*cicle;
				Z=0;
				while(n){
					array[n%10]=true;
					n/=10;
				}
				for(i=0;i<10;i++){
					if(array[i]==false){
						Z=1;
						break;
					}
				}
				if(Z==0){
					printf("Case #%lld: %lld\n",a,N*cicle);
				//	printf("%lld",N*cicle);;
				}
				else
				cicle++;
				
			}
		}
	}
}
