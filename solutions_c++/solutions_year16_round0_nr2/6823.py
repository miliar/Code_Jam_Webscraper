#include <iostream>
#include <string>
using namespace std;

int main() {
	// your code goes here
	long long int t;
	cin>>t;
	
	for (long long int i = 1; i <= t; i++) {
		string s;
		cin>>s;
		long long int x = s.length() - 1;
		long long int flipCount = 0;
		for (long long int q = x; q >= 0; q--) {
			if (s[q] == '-') {
				//flip
				for (long long int j = 0; j <=q; j++) {
					if(s[j] == '+') {
						s[j] = '-';
					} else if (s[j] == '-') {
						s[j] = '+';
					}
				}
				flipCount++;
			} else {
				continue;
			}
		}
		cout<<"Case #"<<i<<": "<<flipCount<<endl;
	}
	return 0;
}