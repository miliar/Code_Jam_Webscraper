#include <iostream>
#include <stdio.h>
#include <string>
#include <math.h>

using namespace std;
int main() {
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	long long T,K,C,S,P,A;
	cin>>T;
	for(int j=0;j<T;j++) {
		cin>>K>>C>>S;
		cout<<"Case #"<<(j+1)<<":";
		P = 1;
		for(int i=0;i<C-1;i++)	P*=K;
		A = 0;
		for(int i=0;i<S;i++) {
			cout<<" "<<(A+1);
			A+=P;
		}
		cout<<endl;
	}
	return 0;
}