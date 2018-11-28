#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;
int main() {
	int t;
	long long n;
	scanf("%d",&t);
	int check[10];
	
	for(int i=1;i<=t;i++) {
		cin>>n;
		if(n==0) {
			printf("CASE #%d: INSOMNIA\n",i);
			continue;
		}
		long long multiplier =1;
		memset(check,0,sizeof(check));
		while(1) {
			int count=0;
			for(int i=0;i<10;i++) {				
				if(check[i]==0) {
					count++;
				}
			}
			if(count==0) {
				multiplier--;
				break;
			}
			long long num = multiplier*n;
			while(num!=0) {
				check[num%10]=1;
				num/=10;
			}
			multiplier++;
		}
		cout<<"CASE #"<<i<<": "<<multiplier*n<<endl;
		
	}	
}
