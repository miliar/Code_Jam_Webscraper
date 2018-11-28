#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:30000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <queue>
#include <vector>

using namespace std;

const double EPS = 1E-8;
const int INF = (int)1E+9;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forv(i, v) for (int i = 0; i < (int)(v.size()); ++i)
#define fors(i, s) for (int i = 0; i < (int)(s.length()); ++i)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair

typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long ll;
typedef long double ld;

bool isPal(const int & num) {
	stringstream ss;
	ss << num;
	string str;
	ss >> str;
	for (int i = 0; i < str.length(); ++i)
		if (str[i] != str[str.length() - 1 - i])
			return false;
	return true;
}

bool isPal2(const int & num) {
	int sqrt_num = static_cast<int>(sqrt(num));
	if (sqrt_num * sqrt_num == num)
		return isPal(sqrt_num);
	return false;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	cin >> tests;
	forn(test, tests) {
		int ans = 0;
		int s, t;
		cin >> s >> t;
		for (int i = s; i <= t; ++i)
			ans += isPal(i) && isPal2(i);
		cout << "Case #" << test + 1 << ": " << ans << "\n";
	}
	return 0;
}
