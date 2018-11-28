#pragma comment(linker, "/STACK:100000000")
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;
#define int64 long long
#define ldb long double
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define taskname "task_b"
const ldb pi = acos(-1.0);
const int N = 1000;
int t, n, m, a[N][N];

int main() {
//	assert(freopen(taskname".in", "r", stdin));
//	assert(freopen(taskname".out", "w", stdout));
	scanf("%d", &t);
	for (int it = 0; it < t; ++it) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				scanf("%d", &a[i][j]);
		bool bad = false;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j) {
				bool good = true;
				for (int k = 0; k < m; ++k)
					good &= (a[i][k] <= a[i][j]);
				if (good)
					continue;
				good = true;
				for (int k = 0; k < n; ++k)
					good &= (a[k][j] <= a[i][j]);
				if (good)
					continue;
				bad = true;
			}
		printf("Case #%d: %s\n", it + 1, bad ? "NO" : "YES");
	}	
	return 0;
}