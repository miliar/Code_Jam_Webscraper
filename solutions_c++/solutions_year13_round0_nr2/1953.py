#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
const double pi = acos(-1.0);
const int size = 1000;

int a[size][size];
int hor[size], ver[size];

int main() {
	int tc, n, m;

	freopen("problem_b.in", "r", stdin);
	freopen("problem_b.out", "w", stdout);
	
	cin >> tc;
	for (int tnum = 0; tnum < tc; tnum++) {
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			hor[i] = 0;
		for (int j = 0; j < m; j++)
			ver[j] = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++) {
				cin >> a[i][j];
				hor[i] = max(hor[i], a[i][j]);
				ver[j] = max(ver[j], a[i][j]);
			}
		bool flag = true;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				flag = flag && (a[i][j] == min(hor[i], ver[j]));
		printf("Case #%d: %s\n", tnum + 1, (flag ? "YES" : "NO"));
	}

	return 0;
}