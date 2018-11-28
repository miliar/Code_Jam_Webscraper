#include<bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin>>t;
	for(int cases = 1;cases<=t;cases++) {
		int n;
		cin>>n;
		int count = 0;
		if(n==0) {
			cout<<"Case #"<<cases<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		bool arr[10];
		memset(arr,0,sizeof(arr));
		for(int i=1;;i++) {
			int temp = n * i;
			while(temp!=0) {
				if(arr[temp%10]==0) {
					arr[temp%10]=1;
					count++;
				}
				temp = temp/10;
			}
			if(count==10){
				cout<<"Case #"<<cases<<": "<<n*i<<endl;
				break;	
			}
		}
	}
	return 0;
}
