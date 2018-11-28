
#include<iostream>
#include<cmath>
using namespace std;

int check(int dig[]){
	
	for(int i=0;i<10;i++){
		if(dig[i]==0){
			return 0;
		}
	}
	return 1;
}
void update(int dig[],long long int n){
	int rem;
	while(n>0){
		rem=n%10;
		if(dig[rem]==0){
			dig[rem]++;
		}
		n=n/10;
	}
}
void print(int dig[]){
	for(int i=0;i<10;i++){
		printf("%d ",dig[i]);
	}
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	long long int t;
	
	scanf("%lld",&t);
	for(int i=1;i<=t;i++){
		int dig[10]={0};
		long long int n,sol=0,count=0,fix;
		scanf("%lld",&n);
		fix=n;
		if(n==0){
			printf("Case #%lld: INSOMNIA\n",i);
		}else{
			while(check(dig)==0){
				sol=n;
				update(dig,n);
				count++;
				//print(dig);
				//printf("\n");
				n=fix*(count+1);
			}
			printf("Case #%lld: %lld\n",i,sol);
		}
		
	}
	return 0;
}
