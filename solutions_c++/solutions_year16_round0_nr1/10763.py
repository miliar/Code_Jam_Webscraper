#include<iostream>
using namespace std;
int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
		int n;
		int numbers[10]={0};
		int togo=10;
		cin>>n;
		if(n==0)
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else {
			long long int current=n;
			while(1) {
				long long int temp=current;
				while(temp>0) {
					int unit = temp%10;
					temp/=10;
					if(numbers[unit]==0) {
						numbers[unit]=1;
						togo--;
					}
					if(togo==0)
						break;
				}
				if(togo!=0)
					current+=n;
				else
					break;
			}
			cout<<"Case #"<<i<<": "<<current<<endl;
		}		
	}
	return 0;
}
