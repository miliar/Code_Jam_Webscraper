#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
#define ll long long
#define f first
#define s second
#define mp make_pair
#define pb push_back

using namespace std;

ll T, k, c, s, id;

void solve() {
	id++;
	cin >> k >> c >> s;
	cout << "Case #" << id << ": ";
	for (int i = 1; i <= s; ++i)
		cout << i << ' ';
	cout << endl;
}

int main() {
	#ifdef LOCAL
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	#endif
	cin >> T;
	while (T--) {
		solve();
	}

	return 0;
}
                                

