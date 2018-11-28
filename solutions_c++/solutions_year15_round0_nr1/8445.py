#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cstdlib>
#include <ctime>

using namespace std;

int Case = 1, tc = 0, n = 0;
string s;

long long solve() {
//110011
	long long cur = s[0] - '0', ret = 0;
	for (int i = 1; i < (int) s.size(); i++) {

		if (cur < i) {
			ret += (i - cur);
			cur = i;
		}
		cur += s[i] - '0';
	}
	return ret;
}

int main() {

	freopen("test.in", "rt", stdin);
	freopen("test.out", "w", stdout);

	cin >> tc;

	while (tc--) {

		cin >> n >> s;

		cout << "Case #" << Case++ << ": " << solve() << endl;
	}

	return 0;
}
//By : mohamed waleed
