#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int u = 0; u < t; u++) {
		int sm;
		cin >> sm;
		
		char a[sm+1];
		cin >> a;
		int f = 0;
		int s = 0;
		for (int o = 0; o <= sm && s < sm; o++) {
			int l = a[o] - '0';
			if (o > 0 && l > 0 && o > s) {
				f += o-s;
				s = o;
			}
			s += l;
		}
		cout << "Case #" << u+1 << ": " <<f << endl;
	
	}
	
	
	
	return 0;
}