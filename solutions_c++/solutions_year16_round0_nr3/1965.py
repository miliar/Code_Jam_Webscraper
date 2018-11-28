#include<iostream>
using namespace std;

unsigned long long int power(unsigned long long int b,unsigned long long int n){
	unsigned long long int a=1;
	while(n){
		if(n%2)a*=b;
		b*=b;n/=2;
	}
	return a;
}

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	unsigned long long int t;cin>>t;
	unsigned long long int a,b;cin>>a>>b;
	cout<<"Case #1: "<<endl;
	for(unsigned long long int i=0,j=0;i<b;i++,j=i){
		cout<<"1";
		for(unsigned long long int k=0;k<(a/2)-2;k++){
			cout<<(j%2);j/=2;
		}
		cout<<"11";j=i;
		for(unsigned long long int k=0;k<(a/2)-2;k++){
			cout<<(j%2);j/=2;
		}
		cout<<"1";
		if(a==16)cout<<" 257 6562 65537 390626 1679617 5764802 16777217 43046722 100000001"<<endl;
		if(a==32)cout<<" 65537 43046722 4294967297 152587890626 2821109907457 33232930569602 281474976710657 1853020188851842 10000000000000001"<<endl;
	}
	return 0;
}
