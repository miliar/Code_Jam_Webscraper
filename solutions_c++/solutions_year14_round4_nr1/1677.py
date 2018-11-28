#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define FOR(i,s,e) for (int i = int(s); i < int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define sz(v) (int)v.size()
#define all(c) (c).begin(), (c).end()

typedef long long int ll;

#define NMAX 10005

// %I64d for ll in CF

/*int solve(int i, int full[NMAX], bool used[NMAX], int disks) {
	if (i == n) return disks;

	int res = 1e9;
	for (int j = 0; j < n; j++) {
		if (!used[j] && full[j] + costs[i] <= x) {
			bool full0 = full[j] > 0;
			if (full0) used[j] = true;
			full[j] += costs[i];
			res = min(res, solve(i + 1, full, used, disks + (!full0 ? 1 : 0)));
			full[j] -= costs[i];
			if (full0) used[j] = false;

			if (full[j] == 0) break;
		}
	}

	return res;
}*/

int main() {
	int t;
	scanf("%d", &t);
	for (int q = 1; q <= t; q++) {
		int n, x;
		scanf("%d %d", &n, &x);
		int costs[NMAX];
		for (int i = 0; i < n; i++) {
			scanf("%d", &costs[i]);
		}

		sort(costs, costs + n);
		reverse(costs, costs + n);
		int disks = 0;
		int front = 0, last = n - 1;
		bool done[n];
		memset(done, false, sizeof done);
		while (!done[front] && front <= last) {
			//printf("%d %d\n", front, last);
			disks++;
			done[front] = true;
			if (!done[last] && costs[front] + costs[last] <= x) {
				done[last] = true;
				last--;
			}
			front++;
		}

		/*int full[NMAX];
		memset(full, 0, sizeof full);
		bool used[NMAX];
		memset(used, false, sizeof used);
		printf("Case #%d: %d\n", q, solve(0, full, used, 0));*/
		printf("Case #%d: %d\n", q, disks);
	}
	return 0;
}
