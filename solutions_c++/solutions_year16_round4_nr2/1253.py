#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

double cmp(vector<double>& PP) {
	vector<pair<int, double>> P1, P2;
	P2.push_back(make_pair(0, 1));
	for (auto& p : PP) {
		P1 = P2;
		P2.clear();
		for (auto& t : P1) {
			P2.push_back(make_pair(t.first + 1, t.second * p));
			P2.push_back(make_pair(t.first - 1, t.second * (1-p)));
		}
	}
	double ret = 0;
	for (auto& t : P2) {
		if (t.first == 0 /*&& t.second > ret*/) ret += t.second;
	}
	return ret;
}

double solve(vector<double>& P, int K) {
	int N = P.size();
	double ret = 0;
	for (int i = 0; i < (1 << N); ++i) {
		int cnt = 0;
		for (int j = 0; j < N; ++j) if (i&(1 << j)) ++cnt;
		if (cnt != K) continue;
		vector<double> PP;
		for (int j = 0; j < N; ++j) if (i&(1 << j)) PP.push_back(P[j]);
		double r = cmp(PP);
		if (r > ret) ret = r;
	}
	return ret;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N, K;
		cin >> N >> K;
		vector<double> P(N);
		for (auto& p : P) cin >> p;

		double ret = solve(P, K);
		cout << "Case #" << t << ": " << ret << endl;
	}
	return 0;
}