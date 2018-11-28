#include<iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int c=1; c<=t; c++) {
		string s;
		cin >> s;
		int ret=0;
		char state = '+';
		for (int i=s.size()-1;i>=0;i--) {
			if(s[i] != state) {
				ret++;
				state=s[i];
			}
		}
		cout << "Case #" << c << ": " << ret << endl;
	}
	return 0;
}
