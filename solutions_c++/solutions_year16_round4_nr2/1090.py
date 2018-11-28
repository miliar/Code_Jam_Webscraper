//============================================================================
// Name        : A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <map>
#include <cstdio>
#include <queue>
#include <set>
#include <vector>
typedef long long LL;
using namespace std;
#define MAXN 210
double p[MAXN];

vector<int> o[1 << 16];

int one(int x) {
	int cnt = 0;
	while (x) {
		cnt += x & 1;
		x >>= 1;
	}
	return cnt;
}
double gao(int N, int K, int s) {
	double g[MAXN];
	int j = 0;
	double ans = 0;
	for (int i = 0; i < N; i++) {
		if (s & (1 << i)) {
			g[j++] = p[i];
		}
	}
	for (int i = 0; i < 1 << K; i++) {
		if (one(i) == K / 2) {
			double tmp = 1;
			for (int j = 0; j < K; j++) {
				if (i & (1 << j)) {
					tmp *= g[j];
				} else {
					tmp *= (1 - g[j]);
				}
			}
			ans += tmp;
		}
	}
	return ans;
}
int main() {
	int T;
	string path = "/Users/baidu/Downloads/";

//change file name
	string in = "B-small-attempt0.in";
	string out = "0.txt";

	freopen((path + in).c_str(), "r", stdin);
	freopen((path + out).c_str(), "w", stdout);
	cin >> T;
	for (int t = 1; t <= T; ++t) {

		int N, K;
		cin >> N >> K;
		for (int i = 0; i < N; i++) {
			cin >> p[i];
		}

		double p = 0;
		for (int i = 1; i < 1 << N; i++) {
			if (one(i) == K) {
				p = max(p, gao(N, K, i));
			}
		}

		printf("Case #%d: %.8lf\n", t, p);

//		cout << "Case #" << t << ": " << p << endl;
	}
	return 0;
}
