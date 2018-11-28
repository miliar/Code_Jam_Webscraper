#include<cstdio>
using namespace std;

int main(){
	int t;
	long long n;
	scanf("%d",&t);
	for(int j=1;j<=t;j++){
		scanf("%lld",&n);
		int count=0;
		if(n==0)
			printf("Case #%d: %s\n",j,"INSOMNIA");
		else{
			bool arr[10]={0};
			int i=1;
			while(count!=10){
				long long temp=n*i;
				while(temp!=0){
					int rem=temp%10;
					if(!arr[rem]){
						arr[rem]=true;
						count++;
					}
					temp/=10;
				}
				i++;
			}
			printf("Case #%d: %lld\n",j,n*(i-1));
		}
	}
	return 0;
}
				
			
		
