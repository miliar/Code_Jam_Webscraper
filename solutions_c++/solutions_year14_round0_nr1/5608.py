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
#define taskname "task_a"
const ldb pi = acos(-1.0);
const int m = 2;
const int n = 4;

int main() {
	assert(freopen(taskname".in", "r", stdin));
	assert(freopen(taskname".out", "w", stdout));
	int t, num, r[m], where[m][n * n];
	scanf("%d", &t);
	for (int it = 0; it < t; ++it) {
		for (int i = 0; i < 2; ++i) {
			scanf("%d", &r[i]), --r[i];
			for (int x = 0; x < n; ++x)
				for (int y = 0; y < n; ++y)
					scanf("%d", &num), --num, where[i][num] = x;
		}
		vector<int> ans;
		for (int x = 0; x < n * n; ++x) {
			bool done = true;
			for (int i = 0; i < 2; ++i)
				done &= (where[i][x] == r[i]);
			if (done) ans.pb(x);
		}
		printf("Case #%d: ", it + 1);
		if (ans.empty()) {
			printf("Volunteer cheated!\n");
			continue;
		}
		if (sz(ans) > 1) {
			printf("Bad magician!\n");
			continue;
		}
		printf("%d\n", ans[0] + 1);
	}
	return 0;
}