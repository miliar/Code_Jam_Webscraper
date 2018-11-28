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


void solveTest(int test) {
    double cost, feed, target;
    fscanf(in, "%lf %lf %lf", &cost, &feed, &target);
    double ans = 0.0;
    double curFeed = 2.0;
    while (true) {
        double need = target / curFeed;
        double oneed = cost / curFeed + target / (curFeed + feed);
        if (need < oneed)
            break;
        ans += cost / curFeed;
        curFeed += feed;
    }
    ans += target / curFeed;
    fprintf(out, "%.9lf\n", ans);
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("CookieClickerAlpha.in", "rt");
	out = fopen("CookieClickerAlpha.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++) {
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		solveTest(test);
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n", (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	return 0;
}
