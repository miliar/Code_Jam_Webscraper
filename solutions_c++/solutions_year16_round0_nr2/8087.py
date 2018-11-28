#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <functional>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>

#define rep(i, a) REP(i, 0, a)
#define REP(i, a, b) for(int i = a; i < b; ++i)
#define rrep(i, a) RREP(i, a, 0)
#define RREP(i, a, b) for(int i = a; i >= b; --i)
#define repll(i, a) REPLL(i, 0, a)
#define REPLL(i, a, b) for(ll i = a; i < b; ++i)
#define rrepll(i, a) RREPLL(i, a, 0)
#define RREPLL(i, a, b) for(ll i = a; i >= b; --i)

typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<int, int> P;
typedef std::pair<P, int> PP;
const double PI = 3.14159265358979323846;
const double eps = 1e-9;
const int infi = (int)1e+9 + 10;
const ll infll = (ll)1e+17 + 10;

int num(std::string str) {
	int res = 1;
	char c = str[0];
	int i = 1;
	while (i != str.size()) {
		if (c != str[i])++res, c = str[i];
		++i;
	}
	return res;
}

int main() {
	int t;
	std::cin >> t;
	rep(i, t) {
		std::string str;
		std::cin >> str;

		int k = num(str);
		if (str[0] == '+') {
			printf("Case #%d: %d\n", i + 1, (k % 2 ? k - 1 : k));
		}
		else {
			printf("Case #%d: %d\n", i + 1, (k % 2 ? k : k - 1));
		}
	}

	return 0;
}