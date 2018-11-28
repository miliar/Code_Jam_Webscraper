#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <cassert>
#include <cfloat>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iostream>
#include <limits.h>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

#define rep(i,m) for(int i=0;i<(int)(m);++i)
#define sz(c) (int((c).size()))
#define fill(a,b) memset(a,b,sizeof(a))
#define all(x) (x).begin(),(x).end()
#define mp make_pair

int K, L, S;
string key, trg;
double a, b;
int mx;

void go(string s) {
	if (sz(s) == S) {
		b += 1;
		int cur = 0;
		for (int i = 0; i < sz(s); ++i) {
			if (i + sz(trg) > sz(s)) continue;
			if (s.substr(i, sz(trg)) == trg) cur += 1;
		}
		mx = max(mx, cur);
		a += cur;
	} else {
		for (int i = 0; i < sz(key); ++i) {
			go(s + key[i]);
		}
	}
}

void solve(int cur_case) {
	cin >> K >> L >> S >> key >> trg;
	a = b = mx = 0;
	go("");
	double ans = 0;
	if (mx != 0) {
		ans = mx - a / b;
	}
	cout << "Case #" << cur_case << ": " << ans << endl;
}

int main(int argc, char *argv[]) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.precision(10);
	cout << fixed;
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	clock_t start_time = clock(), check_time;
	int total_cases;
	cin >> total_cases;
	for (int cur_case = 1; cur_case <= total_cases; ++cur_case) {
		solve(cur_case);
		check_time = clock(); cerr << "Case #" << cur_case << " elapsed time: " << check_time - start_time << "ms" << endl; start_time = clock();
	}
	return 0;
}
