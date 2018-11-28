#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

#define GET(mask, i, j) ((mask) & 1 << ((i) * n + (j)))

using namespace std;

int n;
bool know[30][30];

int weight(int mask) {
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		if (mask & (1 << i)) ans++;
	}
	return ans;
}

int main() {
	int t; cin >> t;
	for (int test = 1; test <= t; ++test) {
		cin >> n;
		int initial = 0;
		int base = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				char ch; cin >> ch;
				know[i][j] = (ch == '1');
				if (know[i][j]) {
					initial++;
					base |= (1 << (i * n + j));
				}
			}
		}

		int cost = n*n;
		// supersets of base
		for (int mask = base; mask < (1 << (n*n)); mask = ((mask + 1) | base)) {
			int curr_cost = -initial;
			bool mm[5][5];
			vector<int> rows(n);
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < n; ++j) {
					mm[i][j] = GET(mask, i, j);
					//cout << (mm[i][j]) ? '1' : '0';
					if (mm[i][j]) {
						rows[i] |= (1 << j);
						curr_cost++;
					}
				}
				//cout << endl;
			}
			//cout << curr_cost << endl;
			if (curr_cost > cost) continue;
			
			bool failure = false;
			map<int, int> rev;
			for (int i = 0; i < n && !failure; ++i) {
				for (int j = i + 1; j < n && !failure; ++j) {
					if (i == j) continue;
					if ((rows[i] & rows[j]) && (rows[i] != rows[j])) {
						failure = true; // cout << "Row conflict failure" << endl;
						continue; // no rows can overlap and not match
					}
				}
				rev[rows[i]] |= (1 << i);
			}
			if (failure) continue;
			int total_weight = 0;
			for (map<int, int>::iterator it = rev.begin(); it != rev.end(); ++it) {
				if (weight(it->first) != weight(it->second)) {
					failure = true; // cout << "Weight conflict failure" << endl;
					break;
				}
				total_weight += weight(it->first);
			}
			if (failure || total_weight != n) continue;
			cost = min(cost, curr_cost);
		}
		cout << "Case #" << test << ": " << cost << endl;
	}
	return 0;
}