#include<bits/stdc++.h>
using namespace std;
int o[32], n;
bool b[32][32];

bool dfs(int k, int mask) {
	if(k == n)
		return !mask;
	int i = o[k], c = 0;
	for(int j = 0; j < n; ++j) {
		if(b[i][j] && (mask >> j & 1)) {
			if(!dfs(k+1, mask ^ 1 << j))
				return false;
			++c;
		}
	}
	return c > 0;
}

int cal() {
	cin >> n;
	string a[32];
	for(int i = 0; i < n; ++i)
		cin >> a[i];
	int r = n *n;
	for(int z = 0; z < 1<<n*n; ++z) {
		if(__builtin_popcount(z) >= r)
			continue;
		bool ok = true;
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < n; ++j) {
				if((a[i][j] & 1) && (z >> i*n+j & 1))
					ok = false;
				b[i][j] = (a[i][j] & 1) || (z >> i*n+j & 1);
			}
		if(!ok) continue;
		for(int i = 0; i < n; ++i) o[i] = i;
		do {
			ok &= dfs(0, (1<<n) - 1);
		} while(ok && next_permutation(o, o + n));
		if(!ok) continue;
		r = __builtin_popcount(z);
	}
	return r;
}

int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i)
		printf("Case #%d: %d\n", i, cal());
}
