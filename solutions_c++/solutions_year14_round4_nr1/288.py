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

const int MAX = 10004;

int n, k;
int a[MAX];

void solveTest(int test) {
    fscanf(in, "%d %d", &n, &k);
    for (int i = 0; i < n; i++)
        fscanf(in, "%d", &a[i]);
    sort(a, a + n);
    
    int ans = 0;
    int left = 0, right = n - 1;
    while (left <= right) {
        ans++;
        if (a[left] + a[right] <= k && left < right) {
            left++;
            right--;
        }
        else {
            right--;
        }
    }
    fprintf(out, "%d\n", ans);
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("DataPacking.in", "rt");
	out = fopen("DataPacking.out", "wt");
	
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
