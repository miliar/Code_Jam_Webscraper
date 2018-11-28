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

int x, r, c;

void solve(int cur_case) {
	cin >> x >> r >> c;
	bool win = 0;
	if (x == 1) win = 1;
	else if (x == 2) win = (r * c % 2 == 0);
	else if (x == 3) {
		if (r == 1 && c == 1) win = 0;
		if (r == 1 && c == 2) win = 0;
		if (r == 1 && c == 3) win = 0;
		if (r == 1 && c == 4) win = 0;
		if (r == 2 && c == 1) win = 0;
		if (r == 2 && c == 2) win = 0;
		if (r == 2 && c == 3) win = 1;
		if (r == 2 && c == 4) win = 0;
		if (r == 3 && c == 1) win = 0;
		if (r == 3 && c == 2) win = 1;
		if (r == 3 && c == 3) win = 1;
		if (r == 3 && c == 4) win = 1;
		if (r == 4 && c == 1) win = 0;
		if (r == 4 && c == 2) win = 0;
		if (r == 4 && c == 3) win = 1;
		if (r == 4 && c == 4) win = 0;
	} else if (x == 4) {
		if (r == 1 && c == 1) win = 0;
		if (r == 1 && c == 2) win = 0;
		if (r == 1 && c == 3) win = 0;
		if (r == 1 && c == 4) win = 0;
		if (r == 2 && c == 1) win = 0;
		if (r == 2 && c == 2) win = 0;
		if (r == 2 && c == 3) win = 0;
		if (r == 2 && c == 4) win = 0;
		if (r == 3 && c == 1) win = 0;
		if (r == 3 && c == 2) win = 0;
		if (r == 3 && c == 3) win = 0;
		if (r == 3 && c == 4) win = 1;
		if (r == 4 && c == 1) win = 0;
		if (r == 4 && c == 2) win = 0;
		if (r == 4 && c == 3) win = 1;
		if (r == 4 && c == 4) win = 1;
	}
	string who = win ? "GABRIEL" : "RICHARD";
	cout << "Case #" << cur_case << ": " << who << endl;
}

int main(int argc, char *argv[]) {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.precision(10);
	cout << fixed;
	freopen("D-small-attempt1.in", "rt", stdin);
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
