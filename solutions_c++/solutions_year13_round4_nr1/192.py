#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
const double pi = acos(-1.0);
const int llen = 50;
const int size = 10 * 1000;
const long long mdl = 1000002013ll;

int o[size], e[size], p[size];
long long sums[size];

struct mylong {
	int body[llen];

	mylong (long long val = 0) {
		for (int i = 0; i < llen; i++) {
			body[i] = val % 10;
			val /= 10;
		}
	}

	int& operator [] (int ps) {
		return body[ps];
	}
};

mylong operator + (mylong &a, mylong &b) {
	mylong c;
	int d = 0;
	for (int i = 0; i < llen; i++) {
		c[i] = a[i] + b[i] + d;
		d = c[i] / 10;
		c[i] %= 10;
	}

	return c;
}

mylong operator - (mylong &a, mylong &b) {
	mylong c;
	for (int i = 0; i < llen; i++) {
		c[i] += a[i] - b[i];
		if (c[i] < 0) {
			c[i] += 10;
			c[i + 1]--;
		}
	}

	return c;
}

mylong operator * (mylong &a, mylong &b) {
	mylong c;
	for (int i = 0; i < llen; i++)
		for (int j = 0; j <= i; j++)
			c[i] += a[j] * b[i - j];
	int d = 0;
	for (int i = 0; i < llen; i++) {
		c[i] += d;
		d = c[i] / 10;
		c[i] %= 10;
	}

	return c;
}

void printmylong(mylong& a) {
	for (int i = llen - 1; i >= 0; i--)
		if (a[i] > 0) {
			for (int j = i; j >= 0; j--)
				printf("%d", a[j]);
			return;
		}
	printf("0");
}

long long getmodulo(mylong& a) {
	long long ans = 0;
	for (int i = llen - 1; i >= 0; i--) {
		ans = (ans * 10 + a[i]) % mdl;
	}

	return ans;
}

long long getcost(long long n, long long o, long long e) {
	return n * (e - o) - (e - o + 1) * (e - o) / 2;
}

int main() {
	freopen("problem_a.in", "r", stdin);
	freopen("problem_a.out", "w", stdout);
	
	int tc, n, m;

	scanf("%d", &tc);
	for (int tnum = 0; tnum < tc; tnum++) {
		scanf("%d%d", &n, &m);
		vector <int> coords;
		for (int i = 0; i < m; i++) {
			scanf("%d%d%d", &o[i], &e[i], &p[i]);
			coords.pb(o[i]);
			coords.pb(e[i]);
		}
		sort(coords.begin(), coords.end());
		coords.resize(unique(coords.begin(), coords.end()) - coords.begin());

		int len = coords.size();
		for (int i = 0; i < len; i++)
			sums[i] = 0;
		mylong eans(0);
		for (int i = 0; i < m; i++) {
			eans = eans + mylong(getcost(n, o[i], e[i])) * mylong(p[i]);
			for (int j = 0; j < len - 1; j++)
				if (coords[j] >= o[i] && coords[j + 1] <= e[i])
					sums[j] += p[i];
		}

		mylong tans(0);
		while (true) {
			int st = -1;
			for (int i = 0; i < len; i++)
				if (sums[i] > 0) {
					st = i;
					break;
				}
			if (st == -1)
				break;
			long long mn = sums[st];
			int fn = st;
			while (sums[fn] > 0) {
				mn = min(mn, sums[fn]);
				fn++;
			}
			tans = tans + mylong(getcost(n, coords[st], coords[fn])) * mylong(mn);
			for (int i = st; i < fn; i++)
				sums[i] -= mn;
		}

		printf("Case #%d: %lld\n", tnum + 1, getmodulo(eans - tans));
	}

	return 0;
}