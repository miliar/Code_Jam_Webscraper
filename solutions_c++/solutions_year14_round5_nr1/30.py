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
#include <string>

using namespace std;
FILE *in; FILE *out;

const int MAX = 1048576;

int n;
long long a[MAX];

string toString(long long num) {
    if (num == 0)
        return "0";
    string sign = "";
    if (num < 0)
        sign = "-", num = -num;
    
    string ret;
    while (num)
        ret += (num % 10 + '0'), num /= 10;
    reverse(ret.begin(), ret.end());
    return sign + ret;
}

void solve(int testNum) {
    int p, q, r, s;
    fscanf(in, "%d %d %d %d %d", &n, &p, &q, &r, &s);
    for (int i = 0; i < n; i++) {
        a[i] = ((long long)i * p + q) % r + s;
    }
//    for (int i = 0; i < n; i++)
//        fprintf(stderr, "%s%c", toString(a[i]).c_str(), i + 1 == n ? '\n' : ' ');
//    system("pause");
    long long all = 0, cur = 0, passed = 0;
    for (int i = 0; i < n; i++)
        all += a[i];
    long long ans = 0;
    for (int left = 0, right = 0; left < n; left++) {
        right = max(left, right);
        while (right < n) {
            long long ncur = cur + a[right];
            long long nrem = all - passed - ncur;
            long long willHave = all - max(passed, max(ncur, nrem));
            long long currHave = all - max(passed, max(cur, all - passed - cur));
            ans = max(ans, max(currHave, willHave));
            if (willHave > currHave)
                cur += a[right++];
            else break;
        }
        passed += a[left];
        cur -= a[left];
    }
    fprintf(out, "%.10lf\n", (double)ans / (double)all);
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("MagicalMarvelousTour.in", "rt");
	out = fopen("MagicalMarvelousTour.out", "wt");
	
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
