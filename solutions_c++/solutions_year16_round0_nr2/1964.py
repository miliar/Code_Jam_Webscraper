#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	
	for (int i = 1; i <= t; ++i) {
		string s;
		cin >> s;
		
		int r = 0;
		int l = s.length();
		
		bool h = false, b = false;
		for (int j = 0; j < l; ++j) {
			if (s[j] == '+') {
				h = true;
				if (b) {
					b = false;
					++r;
				}
			} else {
				b = true;
				if (h) {
					h = false;
					++r;
				}
			}
		}
		if (b) {
			++r;
		}
		
		cout << "Case #" << i << ": " << r << endl;
	}
	
	return 0;
}