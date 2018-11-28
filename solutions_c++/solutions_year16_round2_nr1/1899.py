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
#include <cassert>
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
typedef std::pair<int, P> PP;
const double PI = 3.14159265358979323846;
const double eps = 1e-9;
const int infi = (int)1e+9 + 7;
const ll infll = (ll)1e+17 + 7;

char a[] = { 'Z','X','W','G','T','R','O','F','I','S' };
int b[] = { 0,6,2,8,3,4,1,5,9,7 };
std::string c[] = { "ZERO","SIX","TWO","EIGHT","THREE","FOUR","ONE","FIVE","NINE","SEVEN" };

int main() {
	int n;
	std::cin >> n;
	rep(i, n) {
		std::vector<int> v;
		std::string str;
		std::cin >> str;
		int num[27];
		rep(j, 27)num[j] = 0;
		rep(j, str.size()) {
			++num[str[j] - 'A'];
		}

		for (int j = 0; j < 10;++j) {
			while (num[a[j] - 'A'] != 0) {
				rep(k, c[j].size())--num[c[j][k] - 'A'];
				v.push_back(b[j]);
			}
		}

		std::sort(v.begin(), v.end());

		std::cout << "Case #" << i + 1 << ": ";
		rep(i, v.size()) {
			std::cout << v[i];
		}
		std::cout << std::endl;
	}

	return 0;
}