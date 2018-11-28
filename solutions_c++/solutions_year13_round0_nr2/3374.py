#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define maxl 510
#define ll long long
#define INF 0x3f3f3f3f

using namespace std;

int n, m;
int dr[4] = {0, 0, 1, -1};
int dc[4] = {1, -1, 0, 0};
int a[maxl][maxl];

bool check(int r, int c) {
	int nr = r, nc = c;
	int f1 = 1, f2 = 1;
	for(int i=0; i<n; ++i) {
		if(a[i][c] > a[r][c]) f1 = 0;
	}
	for(int j=0; j<m; ++j) {
		if(a[r][j] > a[r][c]) f2 = 0;
	}
	return (f1 || f2);
}

bool solve() {
	for(int i=0; i<n; ++i) {
		for(int j=0; j<m; ++j) {
			if(!check(i, j)) return 0;
		}
	}
	return 1;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int q=1; q<=t; ++q) {
		scanf("%d%d", &n, &m);
		for(int i=0; i<n; ++i) {
			for(int j=0; j<m; ++j) {
				scanf("%d", &a[i][j]);
			}
		}

		printf("Case #%d: %s\n", q, solve() ? "YES" : "NO");
	}

	return 0;
}


