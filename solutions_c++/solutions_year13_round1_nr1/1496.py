#include<string>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

int T;
double r, t;
long long minv, maxv, midv;
double a, b, tt;

void init() {
	cin >> r >> t;
}

int work() {
	minv = 1;
	maxv = 2000000000LL;
	midv = 0;
	while (minv != maxv) {
		midv = (minv + maxv + 1) / 2;
		a = 2 * r + 1;
		b = 2 * r + 1 + 4 * (midv - 1);
		tt = (a + b) * midv / 2;
		if (tt > t)
			maxv = midv - 1;
		else
			minv = midv;
	}
	midv = (maxv + minv) / 2;
	return midv;
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;
	for (int i=1; i<=T; i++) {
		init();
		cout << "Case #" << i << ": " << work() << endl;
	}
	return 0;
}