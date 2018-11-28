#include <iostream>
using namespace std;

int main() {
	long T, k,c,s;
	cin>>T;
	for (long ti = 1; ti <= T; ti++) {
		cout<<"Case #"<<ti<<": ";
		cin>>k>>c>>s;
		int i = 1;
		if (s<k) {
			cout<<"IMPOSSIBLE";
		}
		else {
			for (; i < k; i++) {
				cout<<i<<" ";
			}
			cout<<i;
		}
		cout<<endl;
	}

	return 0;
}