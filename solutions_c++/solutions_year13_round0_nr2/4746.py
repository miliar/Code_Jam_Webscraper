#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;
#define REP(i, n) for (int i = 0; i < n; ++i)
#define TR(i, x) for (typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define PB push_back
#define MP make_pair
typedef long long ll;

const ll MOD = 1e9 + 7;
const int MAXK = 10;

int a[200][200];
int row[200], col[200];
int main() {
	int n, m;
	int test;
	cin >> test;
	for (int cas = 1; cas <= test; ++cas) {
		cin >> n >> m;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				scanf("%d",&a[i][j]);

		REP(i, n) {
			row[i] = 0;
			REP(j, m)
				row[i] = max(row[i], a[i][j]);
		}
		REP(j, m) {
			col[j] = 0;
			REP(i, n)
				col[j] = max(col[j], a[i][j]);
		}

		bool findAnswer = true;
		REP(i, n)
			REP(j, m) {
				if (a[i][j] != min(row[i], col[j])) {
					findAnswer = false;
					break;
				}
			}
		printf("Case #%d: %s\n",cas, findAnswer? "YES" : "NO");
	}
}

