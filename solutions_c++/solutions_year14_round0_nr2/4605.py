#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

inline int readint() {
	char c = getchar();
	while (!isdigit(c)) c = getchar();
	int x = 0;
	while (isdigit(c)) {
		x = x * 10 + c - '0';
		c = getchar();
	}
	return x;
}

inline long long readlong() {
	char c = getchar();
	while (!isdigit(c)) c = getchar();
	long long x = 0;
	while (isdigit(c)) {
		x = x * 10 + c - '0';
		c = getchar();
	}
	return x;
}

#define FOR(i, n) for (int i = 0; i < (int)(n); i++)
#define REP(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define CIR(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define ADJ(i, u) for (int i = hd[u]; i != -1; i = edge[i].nxt)
#define ECH(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++ i)
#define PII pair<int, int>
#define FI first
#define SE second
#define MP make_pair
#define PB push_back
#define SZ(v) v.size()
#define ALL(v) v.begin(), v.end()
#define CLR(v, a) memset(v, a, sizeof(v))
#define IT iterator
#define LL long long
#define DB double
#define PI 3.1415926
#define INF 1000000000

int main() {
	int test;
	double C, F, X;
	cin >> test;

	FOR(cas, test) {

		cin >> C >> F >> X;

		double res = X / 2;

		int cnt = 1;

		while (1) {
			double tmp = 0;
			double v = 2;

			FOR(i, cnt) {
				tmp += C / (2 + F * i);
				v = 2 + F * (i + 1);
			}

			tmp = tmp + X / v;

			if (res > tmp) {
				res = tmp;
			}
			else {
				break;
			}
			cnt++;
		}		

		printf("Case #%d: %.6f\n", cas + 1, res);
	}
	return 0;
}
