#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <memory.h>
#include <vector>
#include <queue>
#include <deque>
#include <string>
#include <stack>
#include <ctime>
#include <set>
#include <map>
#include <list>
#include <memory.h>

using namespace std;

void solve() {
	string s;
	cin >> s;
	int i = s.size() - 1;
	while (i >= 0 && s[i] == '+') {
		--i;
	}
	int ans = 0;
	char c = '+';
	for (; i >= 0; --i) {
		if (c != s[i]) {
			c = s[i];
			++ans;
		}
	}
	cout << ans << endl;
}

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	
	return 0;
}

