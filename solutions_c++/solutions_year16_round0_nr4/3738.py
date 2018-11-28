#include<stdio.h>
int main(){
	long long int i,n,test,p,q,r,j,k,coun=1;
	scanf("%lld",&test);
	while(coun<=test){
		scanf("%lld%lld%lld",&p,&q,&r);
		if(p==1){
			printf("Case #%lld: %lld\n",coun,p);
		}
		else if((q==1 && p!=r) || r<p-1){

			printf("Case #%lld: IMPOSSIBLE\n",coun);
		}
		else{
if(q==1 && p==r){
			printf("Case #%lld:",coun);
			for(int i=1;i<=p;i++){
				printf(" %lld",i);
			}
			printf("\n");
			}
			else{
			printf("Case #%lld:",coun);
				for(int i=1;i<=r && i<p;i++){
				printf(" %lld",i+1);
			}
			printf("\n");
}}coun++;
}return 0;
}
