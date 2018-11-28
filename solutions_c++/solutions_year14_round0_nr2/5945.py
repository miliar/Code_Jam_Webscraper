#include <iostream>
#include <cstring>
#include <vector>
#include <set>
#include <cstdio>
#include <cmath>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cstdlib>

using namespace std;

#define LL long long
#define ULL unsigned long long

#define REP(var, init, limit, inc) for(int var = init; var < limit; var += inc)
#define FF first
#define SS second

typedef pair <int, int> PII;
const LL oo = 1e9 + 5;
const int LM = 1e5 + 5;

class b {
	double C, F, X;

	double solve(double rate) {
		if (X/rate < X/(rate + F) + C/rate)
			return X/rate;

		return min(X/rate, solve(rate + F) + C/rate);
	}

public:
	void init() {
		int T;
		cin >> T;
		REP(test_case, 1, T+1, 1) {
			cin >> C >> F >> X;
			cout << "Case #" << test_case << ": ";
			printf("%0.7lf\n", solve(2));
		}
	}
};
