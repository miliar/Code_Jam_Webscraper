#define _USE_MATH_DEFINES
#include <algorithm>
#include <cstdio>
#include <functional>
#include <iostream>
#include <cfloat>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <time.h>
#include <vector>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> i_i;
typedef pair<ll, int> ll_i;
typedef pair<double, int> d_i;
typedef pair<ll, ll> ll_ll;
typedef pair<double, double> d_d;
struct edge { int u, v; ll w; };

int INF = INT_MAX / 2;
ll MOD = 1000000007;
ll _MOD = 1000000009;
double EPS = 1e-10;

int main() {
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		int N; cin >> N;
		vector<int> c(3); cin >> c[0] >> c[2] >> c[1];
		int x;
		for (x = 0; x < 3; x++) {
			vector<int> a(1, x);
			for (int k = 0; k < N; k++) {
				vector<int> _a;
				for (int x: a) {
					_a.push_back(x);
					_a.push_back((x + 1) % 3);
				}
				a = _a;
			}
			vector<int> _c(3);
			for (int x: a) _c[x]++;
			if (c == _c) {
				string s;
				for (int x: a) s.push_back("RSP"[x]);
				for (int k = 0; k < N; k++) {
					int d = 1<<k;
					for (int i = 0; i < s.length(); i += d * 2)
						if (s.substr(i, d) > s.substr(i + d, d))
							for (int j = 0; j < d; j++)
								swap(s[i + j], s[i + d + j]);
				}
				cout << s;
				break;
			}
		}
		if (x == 3) cout << "IMPOSSIBLE";
		cout << endl;
	}
}
