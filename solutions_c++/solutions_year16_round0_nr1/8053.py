#include <iostream>
#include <cstdio>
using namespace std;
void dosome(unsigned long int n,int a[]){
	while(n>0){
		a[n%10]=1;
		n/=10;
	}	
}
bool check(int a[]){
	bool ans=true;
	for(int i=0;i<10;i++){
		if(a[i]==0){
			ans=false;break;
		}
	}
	return ans;
}
int main() {
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		int n;
		scanf("%d",&n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n",i);
			continue;
		}
		int a[10]={0};
		unsigned long int m = n;
		dosome(m,a);
		while(!check(a)){
			m+=n;
			dosome(m,a);
		}
		cout<<"Case #"<<i<<": "<<m<<endl;
		
	}
	return 0;
}