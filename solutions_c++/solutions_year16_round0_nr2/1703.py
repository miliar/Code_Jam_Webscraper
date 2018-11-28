#include <iostream>
#include <string>

using namespace std;

int main() {
	int t;
	cin>>t;
	for (int tt = 1; tt <= t; ++tt) {
		string s;
		cin>>s;
		int groups = 1;
		for (int i = 1; i < s.size(); ++i) {
			if (s[i] != s[i - 1]) {
				++groups;
			}
		}
		if (s[s.size() - 1] == '+') {
			--groups;
		}
		cout<<"Case #"<<tt<<": "<<groups<<endl;
	}
	return 0;
}
