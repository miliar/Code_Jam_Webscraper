#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <cmath>
#include <vector>

using namespace std;
const int mn = 10000;
int id[mn];
int s[mn], ref[mn];
int t[mn], pos[mn];

int steps(int n, int *id) {
	int t[mn];
	bool found_top = 0;
	for (int i = 0; i < n; ++i) {
		ref[i] = s[id[i]];
		t[i] = s[i];
		if (found_top) {
			if (i > 0 && ref[i] > ref[i - 1])
				return 1 << 30;
		} else {
			if (i > 0 && ref[i] < ref[i - 1])
				found_top = 1;
		}
	}
	int res = 0;
	for (int i = 0; i < n; ++i) {
		if (t[i] != ref[i]) {
			for (int j = i + 1; j < n; ++j)
				if (ref[i] == t[j]) {
					res += j - i;
					for (int k = j; k > i; --k) {
						t[k] = t[k - 1];
					}
					break;
				}
		}
	}
	return res;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("abc.out", "w", stdout);

	int Tn;
	scanf("%d", &Tn);
	for (int Tc = 1; Tc <= Tn; ++Tc) {
		int n;

		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &s[i]);
			t[i] = s[i];
		}
//		sort(t, t + n);
//		for (int i = 0; i < n; ++i) {
//			for (int j = 0; j < n; ++j) {
//				if (s[j] == t[i]) {
//					pos[i] = j;
//					break;
//				}
//			}
//		}

		int ans = 0;
		for (int i = 0; i < n; ++i) {
			int posmin = 0;
			for (int j = 0; j < n - i; ++j)
				if (s[j] < s[posmin])
					posmin = j;
			int nleft = posmin;
			int nright = n - i - posmin - 1;
			if (nleft < nright) {
				ans += nleft;
			} else {
				ans += nright;
			}
			for (int j = posmin; j < n - i - 1; ++j)
				s[j] = s[j + 1];
		}

		printf("Case #%d: %d\n", Tc, ans);
	}
	return 0;
}
