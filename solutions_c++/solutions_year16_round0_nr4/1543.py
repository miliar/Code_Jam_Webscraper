#include<iostream>
using namespace std;

int t,T,i;
int K,C,S;

int main(){
	cin>>T;
	for(t=1;t<=T;++t){
		cin>>K>>C>>S;
		cout<<"Case #"<<t<<": ";
		for(i=1;i<=K;++i)
			cout<<i<<' ';
		cout<<'\n';
	}
}