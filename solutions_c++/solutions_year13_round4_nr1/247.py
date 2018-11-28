#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;
const long long mo = 1000002013;

struct data
{
	int p;
	long long st, num;
};

int ca, tot, m;
long long ans1, ans2, n, x, y, z, tmp, ans;
data a[3000], f[3000];

bool cmp(const data &a, const data &b)
{
	if (a.st != b.st) return a.st < b.st;
	return a.p < b.p;
}

int main()
{
	freopen("a.out","w",stdout);
	cin >> ca;
	for (int t = 1; t <= ca; t++) {
		tot = 0; cin >> n >> m; ans1 = 0;
		for (int i = 0; i < m; i++) {
			cin >> x >> y >> z;
			tmp = n + n - (y - x - 1);
			tmp = tmp * (y - x); tmp = tmp / 2;
			tmp = tmp % mo; tmp = (tmp * z) % mo;
			ans1 = (ans1 + tmp) % mo;
			a[tot].p = 0; a[tot].st = x; a[tot++].num = z;
			a[tot].p = 1; a[tot].st = y; a[tot++].num = z;
		}
		sort(a, a + tot, cmp);
		int sz = 0; ans2 = 0;
		for (int i = 0; i < tot; i++) {
			if (a[i].p == 0) {
				f[++sz] = a[i];
			} else {
				while (a[i].num > 0) {
					z = min(a[i].num, f[sz].num);
					tmp = n + n - (a[i].st - f[sz].st - 1);
					tmp = tmp * (a[i].st - f[sz].st); tmp = tmp / 2;
					tmp = tmp % mo; tmp = (tmp * z) % mo;
					ans2 = (ans2 + tmp) % mo;
					a[i].num -= z; f[sz].num -= z; 
					if (f[sz].num == 0) --sz;
				}
			}
		}
		ans = ((ans1+mo) - ans2) % mo;
		printf("Case #%d: ", t);
		cout << ans << endl;
	}
	return 0;
}

