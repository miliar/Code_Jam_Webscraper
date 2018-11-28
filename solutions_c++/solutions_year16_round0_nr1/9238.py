#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
const int N = 5e5;
const ld EPS = (ld)1e-10;
const ll MOD = (ll) 1e9 + 7;

char used[10];
int k = 0;

void mark(int a) {
	if (a % 10 == 0 && !used[0]) {
		++k;
		used[0] = true;
	}
	while (a) {
		if (!used[a % 10]) {
			used[a % 10] = true;
			++k;
		}
		a /= 10;
	}
}

int ans(int num) {
	int i = 1;
	k = 0;
	fill(used, used + 10, false);
	for (;;++i) {
		mark(i * num);
		if (k == 10) break;
	}
	return i * num;
}

int main() {
	ios_base::sync_with_stdio(0);
#ifdef KOBRA
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
//    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdout);
#endif
	int cases;
	cin >> cases;
	for (int i = 1; i <= cases; ++i) {
		int num;
		cin >> num;
		cout << "Case #" << i << ": ";
		if (!num) {
			cout << "INSOMNIA\n";
		} else {
			cout << ans(num) << '\n';
		}
	}
	return 0;
}
