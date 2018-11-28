#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

long long mod = 1000002013;

long long n;

struct line {
	long long x1;
	long long x2;
	long long p;
	bool operator < (const line& rhs) const {
		if (x1 == rhs.x1) return x2 < rhs.x2;
		return x1 < rhs.x1;
	}
};

int changed(vector<line>& a) {
	int m = (int)a.size();

	for (int i = 1; i < (int)a.size(); ++i) {
		if (a[i].x1 == a[i - 1].x1 && a[i].x2 == a[i - 1].x2) {
			a[i].p += a[i - 1].p;
			a[i - 1].p = 0;
		}
	}

	for (int i = 0; i < m; ++i) {
		if (a[i].p == 0) continue;
		for (int j = i + 1; j < m; ++j) {
			if (a[j].p == 0) continue;
			if (a[j].x1 > a[i].x2) break;
			if (a[i].x1 == a[j].x1) continue;
			if (a[j].x2 <= a[i].x2) continue;

			long long pp = min(a[i].p, a[j].p);
			a[i].p -= pp;
			a[j].p -= pp;

			line tmp;
			tmp.x1 = a[i].x1;
			tmp.x2 = a[j].x2;
			tmp.p = pp;
			a.push_back(tmp);

			tmp.x1 = a[j].x1;
			tmp.x2 = a[i].x2;
			tmp.p = pp;
			a.push_back(tmp);

			return 1;
		}
	}
	return 0;	
}

long long calc(vector<line>& a) {
	long long ret = 0;
	int m = (int)a.size();
	for (int i = 0; i < m; ++i) {
		long long k = a[i].x2 - a[i].x1;
		long long sum = n * k;
		sum -= k * (k - 1) / 2;
		sum = (sum * a[i].p) % mod;
		ret = (ret + sum) % mod;
	}
	return ret;
}

int main() {
	int r;
	scanf("%d", &r);
	for (int cs = 1; cs <= r; ++cs) {
		printf("Case #%d: ", cs);
		int m;
		long long c1, c2;
		scanf("%lld %d\n", &n, &m);
		vector<line> a;
		for (int i = 0; i < m; ++i) {
			line t;
			scanf("%lld %lld %lld", &t.x1, &t.x2, &t.p);
			a.push_back(t);
		}
		
		c1 = calc(a);

		do {
			vector<line> tmp;
			for (int i = 0; i < (int)a.size(); ++i) {
				if (a[i].p == 0) continue;
				if (a[i].x1 == a[i].x2) continue;
				tmp.push_back(a[i]);
			}
			sort(tmp.begin(), tmp.end());
			a = tmp;
		} while (changed(a));

		c2 = calc(a);
		long long sol = c1 - c2;
		while (sol < 0) sol += mod;
		printf("%lld\n", sol);
	}
	return 0;
}
