#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int T, i, j, k, ans=0, K, C, S;
	cin>>T;
	for(k=1; k<=T; ++k) {
		cin>>K>>C>>S;
		cout<<"Case #"<<k<<": ";
		for(i=1; i<=S; ++i)
			cout<<i<<" ";
		cout<<endl;
	}
	return 0;
}