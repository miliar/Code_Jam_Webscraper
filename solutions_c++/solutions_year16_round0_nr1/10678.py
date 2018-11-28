#include<cstdio>



int main(){
	int t,N,i=1,n,a=0,ans=0,count=1;
	
	scanf("%d",&t);
	
	while(i<=t){
		scanf("%d",&N);
		if(N==0)
			printf("case #%d: INSOMNIA\n",i);
		else{
			a=0;
			count=1;
			ans=0;
			while(1){
				n=count*N;
				ans=n;
				while(n){
					a=a|(1<<(n%10));
					n=n/10;
				}
				//printf(" [a= %d] ",a);
				if(a==1023){
					break;
				}
				count++;
			}
			printf("case #%d: %d\n",i,ans);
		}
		i++;
	}
	return 0;
}
