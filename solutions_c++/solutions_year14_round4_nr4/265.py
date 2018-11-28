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
#include <cassert>
#include <cctype>
#include <cmath>
#include <ctime>

using namespace std;
FILE* in; FILE* out;

const int MAX = 1024;
const int LEN = 104;
const int MOD = 1000000007;

int n, m;
string a[MAX];
set <string> s[MAX];

void solveTest(int test) {
    fscanf(in, "%d %d", &n, &m);
    for (int i = 0; i < n; i++) {
        char buff[LEN];
        fscanf(in, "%s", buff);
        a[i] = buff;
    }

    int worst = 0, cnt = 0;
    for (int mask = 0; mask < (1 << (2 * n)); mask++) {
        int okay = true;
        for (int i = 0; i < n; i++) {
            int group = (!!(mask & (1 << (i * 2 + 0)))) * 1 +
                        (!!(mask & (1 << (i * 2 + 1)))) * 2;
            if (group > m - 1) {
                okay = false;
                break;
            }
        }
        if (!okay)
            continue;

        for (int i = 0; i < m; i++)
            s[i].clear();
        for (int i = 0; i < n; i++) {
            int group = (!!(mask & (1 << (i * 2 + 0)))) * 1 +
                        (!!(mask & (1 << (i * 2 + 1)))) * 2;
//            fprintf(stderr, "%d%c", group, i + 1 == n ? '\n' : ' ');
            for (int c = 0; c <= (int)a[i].size(); c++) {
                s[group].insert(a[i].substr(0, c));
            }
        }
        int cur = 0;
        for (int i = 0; i < m; i++)
            cur += (int)s[i].size();
        if (worst < cur) {
            worst = cur;
            cnt = 1;
        }
        else if (worst == cur)
            cnt++;
    }
    fprintf(out, "%d %d\n", worst, cnt);
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("TheSharding.in", "rt");
	out = fopen("TheSharding.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++) {
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		solveTest(test);
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n",
        (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	return 0;
}
