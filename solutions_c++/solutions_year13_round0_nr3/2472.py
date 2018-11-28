#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <sstream>
using namespace std;

typedef long long int64;

bool isPlain(int64 x) {
	ostringstream oss;
	oss << x;
	string s = oss.str();
	string rs = s;
	reverse(rs.begin(), rs.end());
	return s == rs;
}

bool check(int64 x) {
	return isPlain(x) && isPlain(x * x);
}

const int64 MAX_VALUE = int64(1e14);

vector<int64> all;

void dfs(int64 a) {
	if (a * a > MAX_VALUE)
		return;
	if (a > 0 && check(a)) {
		all.push_back(a * a);
	}
	for (int i = a ? 0 : 1; i < 4; ++i) {
		dfs(a * 10 + i);
	}
}

int main() {
	dfs(0);
	sort(all.begin(), all.end());

//	for (int i = 0; i < (int) all.size(); ++i) {
//		cout << all[i] << endl;
//	}

	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		int64 a, b;
		cin >> a >> b;
		int ans = upper_bound(all.begin(), all.end(), b)
				- lower_bound(all.begin(), all.end(), a);
		cout << ans << endl;
	}
	return 0;
}
