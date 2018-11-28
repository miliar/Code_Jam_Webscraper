#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

const long long mod = 1000002013LL;

map<long long, long long> tree;
long long stk[10000][2];



long long calc(long long d, long long n) {
	if (d == 0) {
		return 0;
	} else {
		return (n + n - d + 1) * d / 2 % mod;
	}
}

int main() {
	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		cout << "Case #" << t << ": ";
		long long n, m;
		cin >> n >> m;
		long long old = 0;
		tree.clear();
		for (int i = 0; i < m; i++) {
			long long a, b, c;
			cin >> a >> b >> c;
			old = (old + calc(b - a, n) * c) % mod;
			tree[a] += c;
			tree[b] -= c;
		}
		int top = 0;
		long long cost = 0;
		for (map<long long, long long>::iterator it = tree.begin(); it != tree.end(); it++) {
			if (it->second > 0) {
				top++;
				stk[top][0] = it->first;
				stk[top][1] = it->second;
			} else if (it->second < 0) {
				long long cnt = -it->second;
				while (cnt > 0) {
					long long d = min(cnt, stk[top][1]);
					cost = (cost + d * calc(it->first - stk[top][0], n)) % mod;
					cnt -= d;
					stk[top][1] -= d;
					if (stk[top][1] == 0) {
						top--;
					}

				}
			}
		}
		cout << ((old - cost) % mod + mod) % mod << endl;
	}
}