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
FILE* in; FILE* out;

const int MAX = 1024;


void solveTest() {
    int k, c, s;
    fscanf(in, "%d %d %d", &k, &c, &s);
    if (s < k) {
        fprintf(out, "IMPOSSIBLE\n");
        return;
    }

    long long off = 0, cur = 1;
    for (int i = 0; i < c - 1; i++) {
        cur *= k;
        off += cur;
    }
    fprintf(stderr, "off is %lld\n", off);

    for (int i = 0; i < k; i++) {
        long long pos = i * off + i + 1;
        fprintf(out, "%lld%c", pos, i + 1 == k ? '\n' : ' ');
    }
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("Fractiles.in", "rt");
	out = fopen("Fractiles.out", "wt");
	
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
