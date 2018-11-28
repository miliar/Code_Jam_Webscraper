#include <iostream>

using namespace std;

int main() {
	int t;
	cin>>t;
	for (int tt = 1; tt <= t; ++tt) {
		int k, c, s;
		cin>>k>>c>>s;
		cout<<"Case #"<<tt<<":";
		for (int i = 1; i <= k; ++i) {
			cout<<" "<<i;
		}
		cout<<endl;
	}
	return 0;
}
