#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
typedef vector<int> vi_;
typedef long long ll_;
int l, x; string str;

int table[5][5] = {
	{ 0, 0, 0, 0, 0 },
	{ 0, 1, 2, 3, 4 },
	{ 0, 2, -1, 4, -3 },
	{ 0, 3, -4, -1, 2 },
	{ 0, 4, 3, -2, -1 },
};

int memo[10001][3];
int solve(int idx = 0, int stage = 0) { 
	//cout << "idx: " << idx << "    stage: " << stage << endl;
	int& ret = memo[idx][stage];
	if (ret != -1) return ret; 

	for (int i = idx, v = 1; i < l*x; ++i) {
		v = (v > 0 ? 1 : -1) * table[abs(v)][str[i%l] - 'i' + 2];
		if ((stage == 0 && v == 2) || (stage == 1 && v == 3))  {
			if (solve(i+1, stage + 1) == 1) return ret = 1;
		}
		if (i == l*x - 1) {
			if (stage == 2) {
				if (v == 4) return ret = 1;
				else return ret = 0;
			}
			else return ret = 0;
		}
	}
	return ret = 0;
}

int main() {
	freopen("C-small-attempt4.in", "r", stdin);
	int t; 
	cin >> t;
	for (int tloop = 0; tloop < t; ++tloop) {
		memset(memo, -1, sizeof(memo));
		cin >> l >> x >> str;
		if (solve() == 1) cout << "Case #" << tloop + 1 << ": YES" << endl;
		else cout << "Case #" << tloop + 1 << ": NO" << endl;
	}
}
