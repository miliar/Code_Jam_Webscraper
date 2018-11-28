#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:16777216")
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <string>
#include <cassert>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <functional>
using namespace std;
typedef long long LL;
template<class T> T Abs(T x) { return x < 0 ? -x : x; }


void Go() {
	int N, K;
	cin >> N >> K;
	vector<double> P(N);
	for (int i = 0; i < N; i++) {
		cin >> P[i];
	}
	vector<int> cc;
	double bestProb = -1;
	sort(P.begin(), P.end());
	for (int jj = 0; jj <= K; jj++) {
		cc.clear();
		for (int i = 0; i < jj; i++) {
			cc.push_back(i);
		}
		for (int i = 0; i < K - jj; i++) {
			cc.push_back(N - i - 1);
		}
		vector<vector<double>> mem(K + 1, vector<double>(K + 1, -1));
		function<double(int, int)> get = [&](int members, int votedYes)->double {
			if (votedYes < 0 || votedYes > members) {
				return 0;
			}
			auto& res = mem[members][votedYes];
			if (res == -1) {
				if (members == 0 && votedYes == 0) {
					res = 1;
				}
				else {
					res =
						P[cc[members - 1]] * get(members - 1, votedYes - 1) +
						(1 - P[cc[members - 1]]) * get(members - 1, votedYes);
				}
			}
			return res;
		};
		double prob = get(K, K / 2);

		if (prob > bestProb) {
			bestProb = prob;
		}
	}
	cout << fixed << setprecision(10) << bestProb << endl;
}

int main() {
	const string task = "B";
	const string folder = "gcj/2016/2";
	const int attempt = -1;
	const bool dbg = false;

	if (dbg) {
		freopen("inp.txt", "r", stdin);
	}
	else {
		stringstream ss;
		ss << folder << '/' << task;
		if (attempt < 0)
			ss << "-large";
		else
			ss << "-small-attempt" << attempt;
		freopen((ss.str() + ".in").c_str(), "r", stdin);
		freopen((ss.str() + ".out").c_str(), "w", stdout);
	}


	static char tt[128];
	gets(tt);
	int t;
	sscanf(tt, "%d", &t);
	for (int i = 0; i < t; i++) {
		printf("Case #%d: ", i + 1);
		Go();
	}
	return 0;
}
