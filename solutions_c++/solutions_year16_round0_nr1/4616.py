#include<iostream>
using namespace std;
int main(){
	int t,n,prod,temp,j;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n;
		if(n==0){
			cout<<"Case #"<<i<<": INSOMNIA\n";
			continue;
		}
		prod=0;
		bool isThere[10]={false};
		while(1){
			prod++;
			temp=n*prod;
			while(temp){
				isThere[temp%10]=true;
				temp/=10;
			}
			j=0;
			while(j<10){
				if(isThere[j]==false) break;
				j++;
			}
			if(j==10) {
				cout<<"Case #"<<i<<": "<<n*prod<<endl;
				break;
			}
		}

	}
	return 0;
}
