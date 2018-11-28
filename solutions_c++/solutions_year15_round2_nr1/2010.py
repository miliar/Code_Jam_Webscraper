#include<iostream>
#include<vector>
#include<cstdio>

using namespace std;

typedef unsigned long long ull;

ull reverse(ull a) {
	ull b=0;
	while(a) {
		b*=10;
		b+=(a%10);
		a/=10;
	}
	return b;
}

vector<ull> q(1000001,9999999);

int main() {

	int nCases;
	cin>>nCases;
	
	q[0]=0;
	for(int i=1;i<=1000000;i++) {
		ull n1=q[i-1]+1;
		ull n2;
		if(i%10) n2=q[reverse(i)]+1;
		else n2=9999999;
		q[i]=n1>n2?n2:n1;
	}
	
	for(int nCase=1; nCase<=nCases; nCase++) {
		cout<<"Case #"<<nCase<<": ";
		ull N;
		cin>>N;		
		cout<<q[N]<<endl;
		
	}

	return 0;
}
