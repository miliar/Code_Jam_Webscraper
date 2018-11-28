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

const int MAX = 32;

int n;
bool a[MAX][MAX];
int order[MAX];

bool recurse(int idx, int used) {
    if (idx >= n)
        return true;
    int node = order[idx];
    bool found = false;
    for (int i = 0; i < n; i++) {
        if (a[node][i] && !(used & (1 << i))) {
            found = true;
            if (!recurse(idx + 1, used | (1 << i))) {
                return false;
            }
        }
    }
    return found;
}

bool willDoIt() {
    /*
    fprintf(out, "\nBoard:\n");
    for (int i = 0; i < n; i++)
        for (int c = 0; c < n; c++)
            fprintf(out, "%d%c", a[i][c] ? 1 : 0, c + 1 == n ? '\n' : ' ');
    */

    for (int i = 0; i < n; i++)
        order[i] = i;
    do {
        /*
        fprintf(out, "  >> tryig order: ");
        for (int i = 0; i < n; i++)
            fprintf(out, "%d%c", order[i], i + 1 == n ? '\n' : ' ');
        */
        if (!recurse(0, 0)) {
            return false;
        }
    } while(next_permutation(order, order + n));
    return true;
}

int dummy() {
    int smask = 0;
    for (int i = 0; i < n * n; i++)
        if (a[i / n][i % n]) smask |= (1 << i);

    int ans = n * n;
    for (int mask = 0; mask < (1 << (n * n)); mask++) {
        if (mask & smask)
            continue;
        if (ans <= __builtin_popcount(mask))
            continue;

        for (int c = 0; c < n * n; c++)
            if (mask & (1 << c)) a[c / n][c % n] = true;
        if (willDoIt()) {
//            fprintf(stderr, "Okay with mask = %d\n", mask);
            ans = __builtin_popcount(mask);
        }
        for (int c = 0; c < n * n; c++)
            if (mask & (1 << c)) a[c / n][c % n] = false;
    }
    return ans;
}

void solveTest() {
    fscanf(in, "%d", &n);
    for (int i = 0; i < n; i++) {
        char buff[MAX];
        fscanf(in, "%s", buff);
        for (int c = 0; c < n; c++)
            a[i][c] = (buff[c] == '1');
    }
    fprintf(out, "%d\n", dummy());
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("FreeformFactory.in", "rt");
	out = fopen("FreeformFactory.out", "wt");

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
