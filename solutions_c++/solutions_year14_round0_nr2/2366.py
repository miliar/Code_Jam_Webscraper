#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <list>
#include <iomanip>
#include <fstream>
#include <iterator>
#include <unordered_map>

using namespace std;
const int MOD = 1000000007; // check!!!
const int INF = 100000000; //1e8

typedef long long ll;
typedef pair<int, int> Pii;
typedef pair<ll, ll> Pll;

#define FOR(i,n) for(int i = 0; i < (n); i++)
#define sz(c) ((int)(c).size())
#define ten(x) ((int)1e##x)
#define tenll(x) ((ll)1e##x)

int main(){
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		double C, F, X; cin >> C >> F >> X;

		double ans = X / 2.0;
		double add = 0;
		for (int n = 1;; n++) {
			add += C / (2.0 + (n-1) * F);
			double tmp = add + X / (2.0 + n * F);
			if (tmp < ans) ans = tmp;
			else break;
		}
		printf("Case #%d: %.10lf\n", t, ans);
	}

	return 0;
}
