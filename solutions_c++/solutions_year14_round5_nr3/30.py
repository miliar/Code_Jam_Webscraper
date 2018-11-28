#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>

using namespace std;
FILE *in; FILE *out;

const int MAX = 1024;
const int MASK = (1 << 15);

struct Event {
    char action[4];
    int id;
};

int n;
Event a[MAX];
int dyn[MAX][MASK];

int popcount(int n) {
    int ret = 0;
    while (n)
        n &= (n - 1), ret++;
    return ret;
}

int recurse(int idx, int mask) {
    if (idx >= n) {
        return popcount(mask);
    }
    if (dyn[idx][mask] != -1)
        return dyn[idx][mask];
    
    int ans = MAX;
    if (a[idx].action[0] == 'E') {
        if (a[idx].id == -1) {
            for (int i = 0; i < n; i++) if ((mask & (1 << i)) == 0) {
                ans = min(ans, recurse(idx + 1, mask | (1 << i)));
            }
        }
        else {
            if ((mask & (1 << a[idx].id)) == 0)
                ans = min(ans, recurse(idx + 1, mask | (1 << a[idx].id)));
        }
    }
    else {
        if (a[idx].id == -1) {
            for (int i = 0; i < n; i++) if ((mask & (1 << i)) != 0) {
                ans = min(ans, recurse(idx + 1, mask ^ (1 << i)));
            }
        }
        else {
            if ((mask & (1 << a[idx].id)) != 0)
                ans = min(ans, recurse(idx + 1, mask ^ (1 << a[idx].id)));
        }
    }
    return dyn[idx][mask] = ans;
}

void solve(int testNum) {
    fscanf(in, "%d", &n);
    map <int, int> q;
    for (int i = 0; i < n; i++) {
        fscanf(in, "%s %d", a[i].action, &a[i].id);
        a[i].id--;
        if (a[i].id != -1) {
            if (q.find(a[i].id) == q.end()) {
                int id = (int)q.size();
                q[a[i].id] = id;
            }
            a[i].id = q[a[i].id];
        }
    }

    int ans = MAX;
    memset(dyn, -1, sizeof(dyn));
    for (int mask = 0; mask < (1 << n); mask++) {
        int cur = recurse(0, mask);
        if (cur <= n) {
            ans = min(ans, cur);
        }
    }
    if (ans > n)
        fprintf(out, "CRIME TIME\n");
    else
        fprintf(out, "%d\n", ans);
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("CrimeHouse.in", "rt");
	out = fopen("CrimeHouse.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++) {
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		solve(test);
	}
	fprintf(stderr, "Total execution time %.3lf seconds.\n",
        (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	return 0;
}
