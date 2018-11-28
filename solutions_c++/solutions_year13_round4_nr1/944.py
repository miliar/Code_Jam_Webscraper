#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <map>
using namespace std;

const int MOD = 1000002013;

long long calc(int l, int r, long long p) {
		p %= MOD;
		long long N = r - l + 1;
		return  N * (N - 1) / 2 % MOD * p % MOD;
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("a.out", "w", stdout);


	int nc;
	cin >> nc;
	for (int cs = 1; cs <= nc; ++cs) {
		int n, m;
		long long res =  0, tmp = 0;
		scanf("%d%d", &n, &m);
		map<int, int> f;
	//	cout << "ds" << endl;
		for (int i = 0; i < m; ++i) {
			int o, e, p;
			cin >> o >> e >> p;
			f[o] += p;
			f[e] -= p;
			tmp += calc(o, e, p);
		}
		
		while (true) {
			long long cnt = 0, mv = 2000000000LL * 1000000000;
			map<int, int>::iterator it = f.begin();
			while (it->second == 0 && it != f.end()) ++it;
			if (it == f.end()) break;
			int l = it->first;
			for (; it != f.end(); ++it) {
				cnt += it->second;
				if (cnt != 0) mv = min(mv, cnt);
				else {
					res +=  calc(l, it->first, mv);
					f[l] -= mv;
					it->second += mv;
					break;
				}
			}
		}
	//	cout << res << ' ' << tmp << endl;
		cout << "Case #" << cs << ": " << ((res - tmp) % MOD + MOD) % MOD << endl;
	}
	return 0;
}

