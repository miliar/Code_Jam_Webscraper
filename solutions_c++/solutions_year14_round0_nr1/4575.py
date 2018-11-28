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

int mat[5][5];
int vis[20];

int main() {
	int test, a;
	cin >> test;

	FOR(cas, test) {
		cin >> a;

		REP(i, 1, 4) 
			REP(j, 1, 4)
				cin >> mat[i][j];

		CLR(vis, 0);

		REP(i, 1, 4) {
			vis[mat[a][i]] |= 1;
		}

		cin >> a;

		REP(i, 1, 4) 
			REP(j, 1, 4)
				cin >> mat[i][j];

		REP(i, 1, 4) {
			vis[mat[a][i]] |= 2;
		}

		int cnt = 0, res;

		REP(i, 1, 16) {
			if (vis[i] == 3) {
				cnt++;
				res = i;
			}
		}


		printf("Case #%d: ", cas + 1);

		if (cnt == 1)
			printf("%d\n", res);
		else if (cnt == 0)
			puts("Volunteer cheated!");
		else
			puts("Bad magician!");
	}
	return 0;
}
