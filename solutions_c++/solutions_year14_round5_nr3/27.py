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
#define taskname "task_c"
const ldb pi = acos(-1.0);
map<int, int> ids;
bool can[2][1 << 15];
int tc, n, t, id;
char cmd;

int lookup(int id) {
	map<int, int>::iterator it = ids.find(id);
	if (it == ids.end()) {
		int tmp = sz(ids);
		ids[id] = tmp;
		return tmp;
	}
	return it->sc;
}

int main() {
	assert(freopen(taskname".in", "r", stdin));
	assert(freopen(taskname".out", "w", stdout));
	scanf("%d", &tc);
	for (int it = 0; it < tc; ++it) {
		ids.clear();
		scanf("%d", &n), t = 0;
		for (int mask = 0; mask < (1 << n); ++mask)
			can[t][mask] = true;
		for (int i = 0; i < n; ++i, t ^= 1) {
			scanf(" %c%d", &cmd, &id), id--;
			if (id != -1) id = lookup(id);
			for (int mask = 0; mask < (1 << n); ++mask)
				can[t ^ 1][mask] = false;
			for (int mask = 0; mask < (1 << n); ++mask)
				if (can[t][mask]) {
					if (id == -1) {
						if (cmd == 'E') {
							for (int j = 0; j < n; ++j)
								if (!(mask & (1 << j)))
									can[t ^ 1][mask ^ (1 << j)] = true;
						} else {
							for (int j = 0; j < n; ++j)
								if (mask & (1 << j))
									can[t ^ 1][mask ^ (1 << j)] = true;
						}
						continue;	
					}
					if (cmd == 'E') {
						if (mask & (1 << id)) continue;
						can[t ^ 1][mask ^ (1 << id)] = true;
					} else {
						if (!(mask & (1 << id))) continue;
						can[t ^ 1][mask ^ (1 << id)] = true;
					}
				}
		}
		int best = n + 1;
		for (int mask = 0; mask < (1 << n); ++mask)
			if (can[t][mask]) best = min(best, __builtin_popcount(mask));
		printf("Case #%d: ", it + 1);
		(best > n) ? printf("CRIME TIME\n") : printf("%d\n", best);
	}
	return 0;
}

