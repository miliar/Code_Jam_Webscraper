#include<bits/stdc++.h>
using namespace std;

#define PB                      push_back
#define MP                      make_pair
#define ALL(v)                  v.begin(),v.end()
#define SZ(v)					(int)v.size()
#define CLR(v, d)               memset(v, d, sizeof(v))

const int OO = (int) 1e9;
const double EPS = 1e-9;
const int mx_sz = (1 << 10);

int nums1[1001], nums2[1001];
int n;

int dp[mx_sz][mx_sz];

int clc(int msk1, int msk2) {

	int idx = __builtin_popcount(msk1);

	if (idx == n)
		return 0;

	int &ref = dp[msk1][msk2];

	if (ref != -1)
		return ref;

	ref = 0;

	for (int i = 0; i < n; i++)
		if (((1 << i) & msk1) == 0) {
			int idx = -1;
			int idx2 = -1;
			for (int j = 0; j < n; j++)
				if ((((1 << j) & msk2) == 0) && nums2[j] > nums1[i]) {
					idx = j;
					break;
				}
			if (idx == -1) {
				// can not find anyone larger so i must win
				for (int j = n - 1; j >= 0; j--)
					if ((((1 << j) & msk2) == 0)) {
						idx2 = j;
						break;
					}

				ref = max(ref, 1 + clc(msk1 | (1 << i), msk2 | (1 << idx2)));
			}

			else {

				ref = max(ref, clc(msk1 | (1 << i), msk2 | (1 << idx)));

				for (int j = idx + 1; j < n; j++)
					if ((((1 << j) & msk2) == 0))
						ref = max(ref, clc(msk1 | (1 << i), msk2 | (1 << j)));
			}
		}
	return ref;
}

int clc2() {

	vector<int> vis(n);

	int ret = 0;

	for (int i = 0; i < n; i++) {
		int idx = -1;
		for (int j = 0; j < n; j++)
			if (!vis[j] && nums2[j] < nums1[i]) {
				vis[j] = 1;
				idx = j;
				break;
			}
		if (idx != -1)
			ret++;
	}

	return ret;
}

int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int t;
	double tmp;

	cin >> t;

	for (int tt = 1; tt <= t; tt++) {

		cin >> n;

		for (int i = 0; i < n; i++) {
			cin >> tmp;
			nums1[i] = (tmp + EPS) * 100000;
		}
		for (int i = 0; i < n; i++) {
			cin >> tmp;
			nums2[i] = (tmp + EPS) * 100000;
		}

		sort(nums1, nums1 + n);
		sort(nums2, nums2 + n);

		vector<int> vis(n, 0);

		int sc = 0;

		for (int i = 0; i < n; i++) {
			bool lose = false;
			for (int j = 0; j < n; j++)
			if (!vis[j] && nums2[j] > nums1[i]) {
				lose = true;
				vis[j] = 1;
				break;
			}

			if (!lose) {
				for (int j = n - 1; j >= 0; j--)
				if (!vis[j]) {
					vis[j] = 1;
					break;
				}
				sc++;
			}
		}

	//	CLR(dp, -1);
		printf("Case #%d: ", tt);

		printf("%d %d\n", clc2(), sc);

	}

	return 0;
}
