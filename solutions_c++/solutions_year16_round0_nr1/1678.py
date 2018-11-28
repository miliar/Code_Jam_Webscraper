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
    int num, mask = 0;
    fscanf(in, "%d", &num);
    for (int i = 1; i < 1000; i++) {
        for (int tmp = num * i; tmp > 0; tmp /= 10)
            mask |= (1 << (tmp % 10));
        if (mask == (1 << 10) - 1) {
            fprintf(out, "%d\n", num * i);
            return;
        }
    }
    fprintf(out, "INSOMNIA\n");
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("CountingSheep.in", "rt");
	out = fopen("CountingSheep.out", "wt");
	
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
