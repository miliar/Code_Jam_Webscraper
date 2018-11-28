#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>

using namespace std;
FILE* in = stdin; FILE* out = stdout;

const int MAX = 16;

int n, k;
double a[MAX];
int use[MAX];

double dyn[MAX][MAX][MAX];
double recurse(int idx, int yes, int no) {
    if (idx >= n) {
        if (yes + no != k)
            return 0.0;
        return yes == no ? 1.0 : 0.0;
    }
    if (dyn[idx][yes][no] == dyn[idx][yes][no])
        return dyn[idx][yes][no];

    double ans = 0.0;

    // Don't use current one
    if (!use[idx]) {
        ans = recurse(idx + 1, yes, no);
    } else {
        double chanceY = recurse(idx + 1, yes + 1, no) * a[idx];
        double chanceN = recurse(idx + 1, yes, no + 1) * (1.0 - a[idx]);
        ans = chanceY + chanceN;
    }
    /*
    double ans = recurse(idx + 1, yes, no);

    // Use him
    double chanceY = recurse(idx + 1, yes + 1, no) * a[idx];
    double chanceN = recurse(idx + 1, yes, no + 1) * (1.0 - a[idx]);
    fprintf(stderr, "At index %d (yes = %d, no = %d): ans = %lf, chanceY = %lf, chanceN = %lf\n",
        idx, yes, no, ans, chanceY, chanceN);
    ans = max(ans, chanceY + chanceN);
    */

    return dyn[idx][yes][no] = ans;
}

double dummy() {
    double ans = 0.0;
    for (int mask = 0; mask < (1 << n); mask++) {
        if (__builtin_popcount(mask) == k) {
            for (int i = 0; i < n; i++)
                use[i] = !!(mask & (1 << i));
            memset(dyn, -1, sizeof(dyn));
            ans = max(ans, recurse(0, 0, 0));
        }
    }
    return ans;
}

void solveTest() {
    fscanf(in, "%d %d", &n, &k);
    for (int i = 0; i < n; i++)
        fscanf(in, "%lf", &a[i]);
    fprintf(out, "%.9lf\n", dummy());
    /*
    memset(dyn, -1, sizeof(dyn));
    fprintf(out, "%.9lf\n", recurse(0, 0, 0));
    */
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("RedTapeCommittee.in", "rt");
	out = fopen("RedTapeCommittee.out", "wt");

	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++) {
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		solveTest();
	}

	fprintf(stderr, "Total execution time %.3lf seconds.\n",
        (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	return 0;
}
