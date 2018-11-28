#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

#define uchar unsigned char
#define ushort unsigned short
#define ull unsigned ll
#define ll long long
#define ull unsigned ll

#define E 2.718281828
#define PI 3.14159265358979323846264338328

int n, k;
double p[16];

double opt;
double kp[16];

double prob() {
	double res = 0;
	for (int comb = 0; comb < (1 << k); comb++) {
		int cnt = 0, num = comb;
		while (num) {
			if (num & 1)
				cnt++;
			num >>= 1;
		}
		if (cnt != k / 2)
			continue;
		double tmp = 1;
		for (int i = 0; i < k; i++)
			if (comb & (1 << i))
				tmp *= kp[i];
			else
				tmp *= (1 - kp[i]);
		res += tmp;
	}
	return res;
}

void solve() {
	cin >> n >> k;
	for (int i = 0; i < n; i++)
		cin >> p[i];
	opt = 0;
	for (int comb = 0; comb < (1 << n); comb++) {
		int cnt = 0, num = comb;
		while (num) {
			if (num & 1)
				cnt++;
			num >>= 1;
		}
		if (cnt != k)
			continue;
		int len = 0;
		for (int i = 0; i < n; i++)
			if (comb & (1 << i))
				kp[len++] = p[i];
		if (len != k) {
			cout << "what?" << endl;
			return;
		}
		double tmp = prob();
		opt = max(opt, tmp);
	}
	cout << setprecision(10) << opt << endl;
}


int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}