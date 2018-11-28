#include <iostream>

#include <algorithm>
#include <functional>
#include <utility>

#include <cmath>
#include <numeric>
#include <complex>

#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <cassert>

#include <iomanip>
#include <sstream>

#include <cctype>
#include <cstring>
#include <string>

#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>

using namespace std;

typedef unsigned char uchar;
typedef short int sint;
typedef unsigned short int usint;
typedef unsigned int uint;
typedef long long i64;
typedef unsigned long long ui64;
typedef double dbl;
typedef long double ldbl;

#define pb push_back
#define mp make_pair

#define abs(x) ((x) < 0 ? (-(x)) : (x))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))

const long double EPS = 1e-9;
const int iINF = INT_MAX;
const long double ldblINF = 1e100;

const int dd[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
const int dd2[8][2] = {{0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}};

const int P = 1000002013;

const int MAXM = 2000;

int o[MAXM];
int e[MAXM];
int p[MAXM];

pair<int, int> q[MAXM * 2];

int d[MAXM];
int c[MAXM];

int x[MAXM * 2];

pair<int, pair<int, int> > q2[MAXM * 2];

int main() {
	int T; scanf("%d\n", &T);
	for (int tt = 1; tt <= T; ++tt) {
		printf("Case #%d: ", tt);
		int n, m;
		cin >> n >> m;

		i64 result = 0;

		for (int i = 0; i < m; ++i) {
			cin >> o[i] >> e[i] >> p[i];
			--o[i];
			--e[i];
			q[i].first = o[i];
			q[i + m].first = e[i];
			q[i].second = p[i];
			q[i + m].second = -p[i];
			int k = e[i] - o[i];
			result += (p[i] * (((n + (n + 1 - k)) * (i64)k / 2 % P))) % P;
			result %= P;
		}
		sort(q, q + 2 * m);
		int qc = 0;
		for (int i = 0; i < 2 * m; ++i) {
			if (!i || q[i].first != q[i - 1].first || ((q[i].second > 0) != (q[i - 1].second > 0))) {
				q[qc++] = q[i];
			} else {
				q[qc - 1].second += q[i].second;
			}
		}
		int qc2 = 0;
		for (int i = 0; i < qc; ++i) {
			//cout << q[i].first << " " << q[i].second << endl;
			if (!i || q[i].first != q[i - 1].first) {
				q2[qc2].first = q[i].first;
				q2[qc2].second.first = q2[qc2].second.second = 0;
				if (q[i].second < 0) {
					q2[qc2].second.first = q[i].second;
				} else {
					q2[qc2].second.second = q[i].second;
				}
				++qc2;
			} else {
				q2[qc2 - 1].second.second = q[i].second;
			}
		}
		i64 result2 = 0;
		for (int i = 0; i < qc2; ++i) {
			int a = abs(q2[i].second.first);
			int b = abs(q2[i].second.second);
//			cout << q2[i].first << " " << a << " " << b << endl;
			int t = min(a, b);
			a -= t;
			b -= t;
			q2[i].second.first = a;
			q2[i].second.second = b;
			for (int j = i - 1; j >= 0 && a > 0; --j) {
				int t = min(a, abs(q2[j].second.second));
				int k = q2[i].first - q2[j].first;
//				cout << "A "  << k << " " << t << endl;
				result2 += (t * ((n + (n + 1 - k)) * (i64)k / 2) % P) % P;
				result2 %= P;
				a -= t;
				q2[j].second.second -= t;
			}
		}
//		cout << result <<  " " << result2 << endl;
		result -= result2;
//		cout << result << endl;
		result %= P;
		if (result < 0) result += P;
		cout << result << endl;
	}
	return 0;
}
