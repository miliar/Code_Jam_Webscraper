#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int c = 1; c < t+1; ++c) {
		int smax;
		cin >> smax;
		int total = 0;
		int res = 0;
		for (int i = 0; i < smax+1; ++i) {
			char csi;
			cin >> csi;
			int si = csi - '0';
			int friends = max(i - total, 0);
			total += friends + si;
			res += friends;
		}
		cout << "Case #" << c << ": " << res << endl;
	}
}