#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <complex>
#include <time.h>

#define M_PI           3.14159265358979323846

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "1"

#pragma comment(linker, "/STACK:56777216")

typedef unsigned long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef pair<int, int> pii;

int main() {
	freopen(PROBLEM_ID".in", "r", stdin);
	freopen(PROBLEM_ID".out", "w", stdout);
	// getline(cin, name)
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		ll k, c, s;
		cin >> k >> c >> s;
		
		ll step = 1;
		for (int x = 1; x <= c - 1; ++x) {
			step *= k;
		}
		
		cout << "Case #" << i + 1 << ": ";
		ll pos = 0;
		for (int i = 0; i < s; ++i) {
			cout << pos + 1 << " ";
			pos += step;
		}
		cout << endl;
	}

	return 0;
}