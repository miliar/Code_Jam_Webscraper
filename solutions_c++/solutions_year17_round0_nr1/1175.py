#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

#ifdef OLYMP_HXLOCAL
	#define P(expr) (cerr << "[line " << __LINE__ << "] " << #expr << ": " << expr << '\n')
#else
	#define P(expr)
#endif

#define len(arr) ((int)(arr).size())

typedef long long ll;

void solve() {
	string s;
	int k;
	cin >> s >> k;

	for (char &c : s)
		c = (c == '+');

	int answer = 0;
	for (int i = 0; i <= len(s) - k; i++)
		if (s[i] == 0) {
			answer++;
			for (int j = i; j < i + k; j++)
				s[j] ^= 1;
		}
	for (int i = len(s) - k + 1; i < len(s); i++)
		if (s[i] == 0) {
			cout << "IMPOSSIBLE\n";
			return;
		}
	cout << answer << '\n';
}

int main() {
#ifndef OLYMP_HXLOCAL
	cin.tie(0);
	ios_base::sync_with_stdio(false);
#endif

	int T;
    cin >> T;
    for (int no = 1; no <= T; no++) {
		cout << "Case #" << no << ": ";
		solve();
	}
	return 0;
}

