#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int T;
double C, F, X;
const int MAXN = 1000000;

double get_time(int n) {
	if (n == 0) return X / 2.0;
	double time = 0.0;
	double rate = 2.0;
	for (int i = 0; i < n; i++) {
		time += C / rate;
		rate += F;
	}
	return time + X / rate;
}

double minus_get_time(int n) {
	return -get_time(n);
}

int find_answer() {
	int l = 0, r = MAXN;
	while (r - l >= 3) {
		int m1 = l + (r - l) / 3, m2 = r - (r - l) / 3;
		if (minus_get_time(m1) < minus_get_time(m2))
			l = m1;
		else
			r = m2;
	}
	double tmp = max(max(minus_get_time(l), minus_get_time(l+1)), minus_get_time(l+2));
	if (tmp == minus_get_time(l)) {
		return l;
	} else if (tmp == minus_get_time(l+1)) {
		return l+1;
	} else {
		return l+2;
	}
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> C >> F >> X;
		printf("Case #%d: %.9f\n", t + 1, get_time(find_answer()));
	}
	return 0;
}