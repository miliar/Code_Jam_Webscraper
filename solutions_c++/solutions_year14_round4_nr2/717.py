#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> discrete;

int nTest;
int n;
int a[1010], id[1010];
int f[1010][1010];
int fl[1010], fr[1010];
int _fl[1010], _fr[1010];

int main() {

	freopen("B-large.in", "r", stdin);
	//freopen("I.txt", "r", stdin);
	freopen("O.txt", "w", stdout);

	scanf("%d", &nTest);
	for (int test = 1; test <= nTest; test++) {
		scanf("%d", &n);
		discrete.clear();
		for (int i = 1; i <= n; i++) {
			scanf("%d", a + i);
			discrete.push_back(a[i]);
		}
		sort(discrete.begin(), discrete.end());
		for (int i = 1; i <= n; i++) {
			a[i] = lower_bound(discrete.begin(), discrete.end(), a[i]) - discrete.begin() + 1;
			id[a[i]] = i;
		}

		for (int i = 1; i <= n; i++) {
			fl[i] = fr[i] = 0;
			_fl[i] = _fr[i] = 0;
			for (int j = 1; j < i; j++)
				if (a[j] > a[i]) _fl[i]++;
			for (int j = i+1; j < id[n]; j++)
				if (a[j] < a[i]) fl[i]++;
			for (int j = i-1; j > id[n]; j--)
				if (a[j] < a[i]) fr[i]++;
			for (int j = n; j > i; j--)
				if (a[j] > a[i]) _fr[i]++;
		}
		memset(f, 63, sizeof f);
		f[n][0] = 0;
		for (int i = n - 1; i >= 1; i--) {
			int idx, red;
			if (id[i] < id[n]) idx = fl[id[i]], red = _fl[id[i]];
			else idx = fr[id[i]], red = _fr[id[i]];

			for (int j = 0; j <= n - i; j++) {
				if (id[i] < id[n]) {
					f[i][j] = min(f[i][j], f[i + 1][j] + idx + (n-i) - 2*red);
					if (j) f[i][j] = min(f[i][j], f[i + 1][j - 1] + idx);
				}
				else {
					f[i][j] = min(f[i][j], f[i + 1][j] + idx);
					if (j) f[i][j] = min(f[i][j], f[i + 1][j - 1] + idx + (n-i) - 2*red);
				}
			}
		}

		int ret = 1e9;
		for (int i = 0; i < n; i++)
			ret = min(ret, f[1][i]);
		printf("Case #%d: %d\n", test, ret);
	}

	return 0;
}