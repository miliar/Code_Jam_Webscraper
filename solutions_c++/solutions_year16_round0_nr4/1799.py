#include <iostream>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; ++cas) {
		unsigned long long k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << cas << ":";
		unsigned long long disp = 0, kc = 1;
		for (int i = 0; i < c; ++i) {
			disp += kc;
			kc *= k;
		}
		//cerr << "disp: " << disp << endl;
		for (unsigned long long i = 0; i < s; ++i) cout << ' ' << disp*i + 1;
		cout << endl;
	}
}
