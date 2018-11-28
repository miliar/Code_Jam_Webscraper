#include <bits/stdc++.h>
using namespace std;

char s[25][25];

int a[25][25];
int n;
int makeA(int msk) {
	int ind = 0;
	int cost = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++) {
			bool g = msk & (1 << (ind++));
			if (!g && s[i][j] == '1')
				return -1;
			if (g && s[i][j] == '0')
				cost++;
			a[i][j] = g;
		}
	return cost;
}

bool ok(int work, int machine) {
	if (work == 0 && machine == 0)
		return true;
	for (int i = 0; i < n; i++) {
		if (!(work & (1 << i)))
			continue;
		bool o = false;
		for (int j = 0; j < n; j++)
				if (machine & (1 << j))
					if (a[i][j] == 1) {
						o = true;
						if (!ok(work ^ (1 << i), machine ^ (1 << j)))
							return false;
					}
		if (o == false)
			return false;
	}
	return true;
}

int main() {
	ios::sync_with_stdio(false);
	freopen("/home/ahmed/Desktop/Round 2/D/D-small-attempt0.in", "r", stdin);
	freopen("/home/ahmed/Desktop/Round 2/D/D-small-attempt0.out", "w", stdout);

	int id = 1;
	int t; scanf("%d", &t);
	while (t--) {

		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%s", s[i]);
		int ans = n * n;
		for (int msk = 0; msk < (1 << (n * n)); msk++) {
			int cost = makeA(msk);
			if (cost == -1)
				continue;
			if (ok((1 << n) - 1, (1 << n) - 1))
				ans = min(ans, cost);
		}
		cout << "Case #" << id++ << ": " << ans << endl;

	}


	return 0;
}
