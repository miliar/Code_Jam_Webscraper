#include <bits/stdc++.h>
using namespace std;

double p[505];
int n, k;

double mem[205][205][205];
int vis_id;
int vis[205][205][205];

bool ok[205];
double get(int ind, int yes, int no) {
	if (yes > k / 2 || no > k / 2)
		return 0;
	if (ind >= n)
		return 1;
	if (vis[ind][yes][no] == vis_id)
		return mem[ind][yes][no];
	vis[ind][yes][no] = vis_id;
	if (ok[ind])
		return mem[ind][yes][no] = get(ind + 1, yes + 1, no) * p[ind] + get(ind + 1, yes, no + 1) * (1 - p[ind]);
	else
		return mem[ind][yes][no] = get(ind + 1, yes, no);
}


int main() {
	ios::sync_with_stdio(false);
	freopen("/home/ahmed/Desktop/Round 2/B/B-large.in", "r", stdin);
	freopen("/home/ahmed/Desktop/Round 2/B/B-large.out", "w", stdout);

	int id = 1;
	int t; scanf("%d", &t);
	while (t--) {

		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i++)
			scanf("%lf", p + i);

		sort(p, p + n);
		double ans = 0;
		for (int L = 0; L <= k; L++) {
			int R = k - L;
			for (int i = 0; i < n; i++)
				ok[i] = 0;
			for (int i = 0; i < L; i++)
				ok[i] = 1;
			for (int i = n - 1; i >= n - R; i--)
				ok[i] = 1;
			vis_id++;
			ans = max(ans, get(0, 0, 0));
		}

		for (int i = 0; i < n; i++) {
			if (i + k - 1 >= n)
				break;
			for (int j = 0; j < n; j++)
				ok[j] = 0;
			for (int j = i; j < i + k; j++)
				ok[j] = 1;
			vis_id++;
			ans = max(ans, get(0, 0, 0));
		}
		printf("Case #%d: %.9lf\n", id++, ans);
	}


	return 0;
}
