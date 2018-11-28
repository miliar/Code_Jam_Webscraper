#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>


typedef long long ll;
typedef long double ld;

using namespace std;

int solve() {
	int ans = 0;
	string s;
	cin >> s;
	vector<char> vv;
	for (int i = 0; i < (int)s.size(); ++i) {
		if (!vv.empty() && vv.back() == s[i]) {
			vv.pop_back();
			ans += 10;
		}
		else {
			vv.push_back(s[i]);
		}
	}
	ans += 5 * (vv.size() / 2);
	return ans;
}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int i = 0; i < tt; ++i) {
		printf("Case #%d: %d\n", i + 1, solve());
	}
	return 0;
}

