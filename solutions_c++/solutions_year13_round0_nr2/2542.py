#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <complex>
#include <list>
#include <deque>
#include <cassert>
#include <ctime>
using namespace std;

#ifdef WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

const double PI = acos(-1.0); 
const double eps = 1e-12;
const int INF = (1 << 31) - 1;
const ll LLINF = ((ll)1 << 62) - 1;

#define mp make_pair
#define pb push_back
#define sz(x) (int)x.size()
#define X first
#define Y second
#define all(x) x.begin(),x.end()
#define fill(a, x) memset(a, x, sizeof(a));
#define next nexttt
#define prev prevvv
#define y1 y111

int a[111][111];
int maxx[111], maxy[111];

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int n;
	scanf("%d", &n);
	for (int t = 0; t < n; t++) {
		int x, y;
		scanf("%d%d", &x, &y);
		for (int i = 0; i < x; i++) {
			for (int j = 0; j < y; j++) {
				scanf("%d", &a[i][j]);
			}
		}
		memset(maxx, 0, sizeof(maxx));
		memset(maxy, 0, sizeof(maxx));
		printf("Case #%d: ", t + 1);
		for (int i = 0; i < x; i++) {
			for (int j = 0; j < y; j++) {
				maxx[i] = max(maxx[i], a[i][j]);
				maxy[j] = max(maxy[j], a[i][j]);
			}
		}
		bool flag = false;
		for (int i = 0; i < x; i++) {
			for (int j = 0; j < y; j++) {
				if (!((maxx[i] == a[i][j]) || (maxy[j] == a[i][j]))) {
					puts("NO");
					flag = true;
					break;
				}
			}
			if (flag) break;
		}
		if (!flag) puts("YES");

	}

	return 0;
}