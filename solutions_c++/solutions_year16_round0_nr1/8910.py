#include<stdio.h>
int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	long long int t,c=1,n,n1;
	int arr[]={0,0,0,0,0,0,0,0,0,0};
	bool flag=false;
	scanf("%lld",&t);
	while(t--){
		flag= false;
		scanf("%lld",&n);
		if(n==0){
			printf("Case #%lld: INSOMNIA\n",c);
			c++;
			
		}
		else{
			long long loc=1;
			
			while(!flag){
				int count=0;
				n1=n*loc;
				//n1=n;
				while(n1>0){
					arr[n1%10]=1;
					//printf("%d sdf\n",n1%10);
					n1/=10;
				}
				for(int i=0;i<10;i++){
					if(arr[i]==1)
						count++;
				}
				if(count==10){
					flag=true;
					printf("Case #%lld: %lld\n",c,n*loc);
					c++;
				}
				loc++;
			}
				for(int i=0;i<10;i++)
				arr[i]=0;
				
		}
	}
	return 0;
	
}
