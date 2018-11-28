#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cstdio>
#include <cmath>

using namespace std;

#define INF 1000000007

void solve() {
	int S, sum = 0, res = 0;
	string s;
	cin >> S >> s;
	for (int i = 0; i < s.size(); i++) s[i] -= '0';
	if (S != 0) {
		sum += s[0];
		for (int i = 1; i < s.size(); i++) {
			if (i <= sum) sum += s[i];
			else res += min(i - sum, S - sum), sum += s[i] + min(i - sum, S - sum);
			if (S <= sum) break;
		}
	}
	cout << res << '\n';
}

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);
	
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	
	return 0;
}

