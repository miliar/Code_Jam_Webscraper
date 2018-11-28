#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#define mo 1000002013
using namespace std;

struct point
{
	int w, nr;
};

struct inter
{
	int o, e, p;
};

point l[1001], r[1001];
inter a[1001];
int n, m;

bool cmp(const inter& x, const inter& y)
{
	return x.o < y.o;
}

bool cmp_(const point &x, const point &y)
{
	return x.w < y.w;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int test;
	cin >> test;
	
	for (int ite = 1; ite <= test; ++ite) {
		cin >> n >> m;
		long long s = 0;
		for (int i = 0; i < m; ++i) {
			cin >> a[i].o >> a[i].e >> a[i].p;
			long long w = a[i].e - a[i].o;
			w = (w * (w - 1) / 2) % mo;
			w = (w * a[i].p) % mo;
			s = (s + w) % mo;
		}

		long long ans = 0;
		sort(a, a + m, cmp);

		for (int i = 0; i < m;) {
			int last = a[i].e;
			int len = 0;
			while (a[i + len].o <= last && i + len < m) {
				if (a[i + len].e > last)
					last = a[i + len].e;
				++len;
			}
			for (int j = 0; j < len; ++j) {
				l[j].w = a[i + j].o;
				r[j].w = a[i + j].e;
				l[j].nr = r[j].nr = a[i + j].p;
			}
			sort(l, l + len, cmp_);
			sort(r, r + len, cmp_);

			for (int j = len - 1; j >= 0; --j) {
				for (int k = 0; k < len && l[j].nr; ++k)
					if (r[k].w >= l[j].w) {
						if (r[k].nr >= l[j].nr) {
							long long w = r[k].w - l[j].w;
							w = (w * (w - 1) / 2) % mo;
							w = w * l[j].nr % mo;
							ans = (ans + w) % mo;
							r[k].nr -= l[j].nr;
							l[j].nr = 0;
						}
						else {
							long long w = r[k].w - l[j].w;
							w = (w * (w - 1) / 2) % mo;
							w = w * r[k].nr % mo;
							ans = (ans + w) % mo;
							l[j].nr -= r[k].nr;
							r[k].nr = 0;
						}
					}
			}
			i += len;
		}
		
		ans = ans - s;
		if (ans < 0) ans += mo;
		cout << "Case #" << ite << ": " << ans << endl;
	}
	
	return 0;
}
