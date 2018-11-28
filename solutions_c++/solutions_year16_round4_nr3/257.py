#include <bits/stdc++.h>
using namespace std;

void solve() {
	int r, c;
	cin >> r >> c;
	vector<int> love((r + c) * 2);
	for(int &i : love) {
		cin >> i;
	}
	for(int mask = 0; mask < 1 << r * c; ++mask) {
		bool valid = true;
		for(int i = 0; i < (r + c) * 2; i += 2) {
			int y, x, side;
			if(love[i] <= c) {
				y = 0;
				x = love[i] - 1;
				side = 0;
			} else if(love[i] <= r + c) {
				y = love[i] - c - 1;
				x = c - 1;
				side = 1;
			} else if(love[i] <= r + c * 2) {
				y = r - 1;
				x = r + c * 2 - love[i];
				side = 2;
			} else {
				y = (r + c) * 2 - love[i];
				x = 0;
				side = 3;
			}
			while(y >= 0 && y < r && x >= 0 && x < c) {
				if(side == 0) {
					side = mask & 1 << (y * c + x) ? 3 : 1;
					x += mask & 1 << (y * c + x) ? 1 : -1;
				} else if(side == 1) {
					side = mask & 1 << (y * c + x) ? 2 : 0;
					y += mask & 1 << (y * c + x) ? -1 : 1;
				} else if(side == 2) {
					side = mask & 1 << (y * c + x) ? 1 : 3;
					x += mask & 1 << (y * c + x) ? -1 : 1;
				} else {
					side = mask & 1 << (y * c + x) ? 0 : 2;
					y += mask & 1 << (y * c + x) ? 1 : -1;
				}
			}
			int dest;
			if(y < 0) {
				dest = x + 1;
			} else if(x >= c) {
				dest = c + y + 1;
			} else if(y >= r) {
				dest = r + c * 2 - x;
			} else {
				dest = (r + c) * 2 - y;
			}
			if(dest != love[i + 1]) {
				valid = false;
				break;
			}
		}
		if(valid) {
			cout << '\n';
			for(int y = 0; y < r; ++y) {
				for(int x = 0; x < c; ++x) {
					cout << "\\/"[!(mask & 1 << (y * c + x))];
				}
				cout << '\n';
			}
			return;
		}
	}
	cout << "\nIMPOSSIBLE\n";
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ':';
		solve();
	}
	return 0;
}
