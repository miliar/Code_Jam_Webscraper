#include<iostream>
using namespace std;

void solve(int t){
	int k,c,s;
	cin>>k>>c>>s;
	long long m=1;
	for(int i=1;i<c;++i){
		m*=k;
	}
	cout<<"Case #"<<t<<":";
	for(int i=1;i<=k;++i){
		cout<<" ";
		cout<<(long long)m*i;
	}
	cout<<endl;
}

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;++t){
		solve(t);
	}
}