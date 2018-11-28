#include <iostream>
using namespace std;
 
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		int ret = 0;
		int count = 0;
		int smax;
		cin >> smax;
		for (int ii = 0; ii <= smax; ii++) {
			char c;
			cin >> c;
			int d = c - '0';
			if (d) {
				if (count < ii) {
					ret += ii-count;
					count = ii;
				}
				count += d;
			}
		}
		cout << "Case #" << t << ": " << ret << endl;
	}
	return 0;
}