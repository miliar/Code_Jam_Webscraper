#include <algorithm>
#include <iostream>
#include <cstdlib>
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

ll T, n, id;
bool used[10];
const ll maxOperation = (ll)(1e8);

bool check(ll x) {
	while (x > 0) {
		used[x % 10] = true;
		x /= 10;
	}
	for (int i = 0; i < 10; ++i)
		if (!used[i])
			return false;
	return true;
}

void solve() {
	id++;
	cin >> n;
	for (int i = 0; i < 10; ++i)
		used[i] = false;
	if (n == 0) {
		cout << "Case #" << id << ": " << "INSOMNIA" << endl;
		return;
	}

	ll x = n, y = 0;
	while (!check(x)) {
		x += n;
		y++;
		if (y > maxOperation) {
			cout << "Case #" << id << ": " << "INSOMNIA" << endl;
			return;
		}
	}
	cout << "Case #" << id << ": " << x << endl;
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
                                

