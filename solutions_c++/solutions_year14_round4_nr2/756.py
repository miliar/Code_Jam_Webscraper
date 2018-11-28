#include <cstring>
#include <iostream>
using namespace std;
const int MOD = 1000000007;
int testCase, n, m, a[1111], f[1111][1111], p[1111], c[1111];
pair<int, int> b[1111];

int calc_pos(int l, int r, int k)
{
	if (c[k] < l) return c[k];
	return c[k] + r - l + 1;
}

int find(int x)
{
	for (int i = 0; i < n; i ++)
	if (a[i] == x) {
		return i;
	}
	return -1;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testCase);
	for (int Case = 1; Case <= testCase; Case ++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i ++) {
			scanf("%d", &a[i]);
			b[i] = make_pair(a[i], i);
		}
		sort(b, b + n);
		for (int i = 0; i < n; i ++) {
			a[b[i].second] = i;
			p[i] = b[i].second;
		}
		int l = 0, r = n - 1;
		int ret = 0;
		for (int i = 0; i < n; i ++) {
			int k = find(i);
			if (k - l < r - k) {
				for (int j = k; j > l; j --) {
					swap(a[j], a[j - 1]);
					ret ++;
				}
				l ++;
			} else {
				for (int j = k; j < r; j ++) {
					swap(a[j], a[j + 1]);
					ret ++;
				}
				r --;
			}
		}
		printf("Case #%d: %d\n", Case, ret);
	}
	return 0;
}
