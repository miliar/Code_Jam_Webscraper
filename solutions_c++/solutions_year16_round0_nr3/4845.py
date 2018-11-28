#define DEBUG 0
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int arr[16];
ll pown[11][16];

int cnt = 0;

ll convertBase(int base) 
{
	ll n = 0;
	for (int i = 0; i < 16; ++i) {
		if (arr[15 - i]) n += pown[base][i];
	}
	return n;
}

ll isPrime(ll n)
{
	for (ll i = 3; i * i <= n; i += 2) {
		if (n % i == 0) {
			return i;
		}
	}
	return ll(-1);
}

int dfs(int index)
{
	if (index == 15) {
		bool works = true;
		vector<int> divisors;
		for (int base = 2; base <= 10; ++base) {
			ll basen = convertBase(base);
			ll pp = isPrime(basen);
			if (pp == -1) {
				works = false;
			} else {
				divisors.push_back(pp);
			}
		}
		if (works) {
			for (int i = 0; i < 16; ++i) {
				cout << arr[i];
			}
			cout << ' ';
			for (int i = 0; i < 9; ++i) {
				//cout << convertBase(i + 2) << ':';
				cout << divisors[i] << ' ';
			}
			cout << '\n';
			++cnt;
		}
		if (cnt == 50) {
			return 1;
		}
		return 0;
	}

	if (dfs(index + 1)) return 1;
	arr[index] = 1;
	if (dfs(index + 1)) return 1;
	arr[index] = 0;
	return 0;
}

void precomputePowers()
{
	for (int b = 2; b <= 10; ++b) {
		ll cur = 1;
		for (int i = 0; i < 16; ++i) {
			pown[b][i] = cur;
			cur *= b;
		}
	}
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cerr << fixed << setprecision(0);

	if (!DEBUG) {
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	}

	precomputePowers();

	int _c, _start = static_cast<int>(clock());
	cin >> _c;

	for(int _cc = 1; _cc <= _c; ++_cc) {
		int _t = static_cast<int>(clock());
		cout << "Case #" << _cc << ": " << '\n';

		int n, j;
		cin >> n >> j;

		arr[0] = arr[15] = 1;

		dfs(1);

		cerr << "[Case #" << _cc << " complete, " << static_cast<int>(clock() - _t) << " ms, " << 100. * _cc / _c << "%]" << endl;
	}

	cerr << "Total time: " << static_cast<int>(clock() - _start) << " ms" << endl;

	return 0;
}

