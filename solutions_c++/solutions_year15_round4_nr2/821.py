#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
#include <map>

using namespace std;

const int MAXN = 105;
const double err = 1e-9;
int T, N;
long long V, X;
pair<int, int> W[MAXN];

inline int readint() {
	string str;
	cin >> str;
	int ret = 0;
	for(int i = 0 ; i < str.size() ; i++) {
		if (str[i] != '.') {
			ret = (ret * 10) + ((int)(str[i] - '0'));
		}
	}
	return ret;
}

inline bool feasible(double tm) {
	double V_left = V;
	double temp = 0.0;

	for(int i = 0 ; i < N ; i++) {
		double use = min(V_left, W[i].second * tm);
		temp += use * W[i].first;
		V_left -= use;
	}
	if (V_left > 0.0) {return false;}
	if (temp > V * X + err) {return false;}

	V_left = V;
	temp = 0.0;
	for(int i = N - 1 ; i >= 0 ; i--) {
		double use = min(V_left, W[i].second * tm);
		temp += use * W[i].first;
		V_left -= use;
	}
	if (V_left > 0.0) {return false;}
	if (temp < V * X - err) {return false;}
	return true;
}

int main() {
	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		cin >> N;
		V = readint();
		X = readint();
		for(int i = 0 ; i < N ; i++) {
			W[i].second = readint();
			W[i].first = readint();
		}
		sort(W, W + N);
		if (X < W[0].first || X > W[N - 1].first) {
			printf("Case #%d: IMPOSSIBLE\n", t);
		}	else {
			double lo = 0.0;
			double hi = 1.0e11;
			for(int lv = 0 ; lv < 200 ; lv++) {
				double mid = (lo + hi) * 0.5;
				if (feasible(mid)) {
					hi = mid;
				}	else {
					lo = mid;
				}
			}
			printf("Case #%d: %.9lf\n", t, ((hi + lo) * 0.5));
		}
	}	
	return 0;
}
