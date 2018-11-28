#include <iostream>
#include <cmath>
using namespace std;

int main(){
	long t, k, c, s;
	cin>>t;
	for(int i = 1; i <= t; i++){
		cin>>k>>c>>s;
		long l = pow(k, c-1);
		cout<<"Case #"<<i<<":";
		for(int j = 0; j < k; j++) cout<<" "<<l*j + 1;
		cout<<endl;
	}
}