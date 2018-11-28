#include <iostream>
using namespace std;

int main() {
	int t;
	string s;
	cin >> t;
	for(int a = 1; a <= t; a++) {
		cin >> s;
		int count = 0;
		int i = 0;
		while(i < s.length()) {
			int j = i;
			while(i < s.length() && s[i] == '+') {
				i++;
			}
			bool foundPos = ((i - j) > 0);
			j = i;
			while(i < s.length() && s[i] == '-') {
				i++;
			}
			bool foundNeg = ((i - j) > 0);
			if(foundNeg) {
				if(foundPos) {
					count++;
				}
				count++;
			}
		}
		cout << "Case #" << a << ": " << count << endl;
	}
	return 0;
}