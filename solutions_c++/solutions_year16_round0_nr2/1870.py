#include <iostream>
#include <string>
using namespace std;
int main() {
	int T;
	cin >> T;	
	for (int t=1;t<=T;t++) {
		cout << "Case #" << t << ": ";
		string s;
		cin >> s;
		int cnt = 0;
		for (int i=1;i<s.length();i++) {
			if (s[i-1]!=s[i]) cnt ++;
		}
		if (s.back() == '-') cnt ++;
		cout << cnt;
		cout << endl;
	}
}