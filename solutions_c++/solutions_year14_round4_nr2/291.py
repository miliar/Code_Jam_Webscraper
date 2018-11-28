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
const int INF = 1000000001;

int n;
int a[MAX];

int calcUp(int left, int right) {
    if (left >= right)
        return 0;
    int ret = 0;
    int tmp[MAX], k = 0;
    for (int i = left; i <= right; i++)
        tmp[k++] = a[i];
    for (int i = 0; i < k; i++) {
        for (int c = 0; c + 1 < k; c++) {
            if (tmp[c] > tmp[c + 1]) {
                ret++;
                swap(tmp[c], tmp[c + 1]);
            }
        }
    }
    return ret;
}

int calcDown(int left, int right) {
    if (left >= right)
        return 0;
    int ret = 0;
    int tmp[MAX], k = 0;
    for (int i = left; i <= right; i++)
        tmp[k++] = a[i];
    for (int i = 0; i < k; i++) {
        for (int c = 0; c + 1 < k; c++) {
            if (tmp[c] < tmp[c + 1]) {
                ret++;
                swap(tmp[c], tmp[c + 1]);
            }
        }
    }
    return ret;
}

int calc(int tmp[MAX]) {
    set < pair <int, int> > s;
    for (int i = 0; i < n; i++) {
        for (int c = i + 1; c < n; c++)
            s.insert(make_pair(tmp[i], tmp[c]));
    }
    int ret = 0;
    for (int i = 0; i < n; i++) {
        for (int c = i + 1; c < n; c++) {
            if (s.find(make_pair(a[i], a[c])) == s.end())
                ret++;
        }
    }
    return ret;
}

/*
int eval(int idx) {
    int tmp[MAX], k = 0;
    for (int i = 0; i < n; i++) {
        if (i < idx && a[i] < a[idx])
            tmp[k++] = a[i];
        if (i > idx && a[i] < a[idx])
            tmp[k++] = a[i];
    }
        if (a[i] < bound) tmp[k++] = a[i];
    sort(tmp, tmp + k);
    tmp[k++] = bound;
    int lim = k;
    for (int i = 0; i < n; i++)
        if (a[i] > bound) tmp[k++] = a[i];
    sort(tmp + lim, tmp + n);
    reverse(tmp + lim, tmp + n);
    for (int i = 0; i < n; i++)
        fprintf(stderr, "%d%c", tmp[i], i + 1 == n ? '\n' : ' ');
    return calc(tmp);
}
*/

/*
int eval() {
    int ret = 0;
    for (int i = 0; i < n; i++) {
        int left = 0, right = n - 1;
        while (left < i && a[left] < a[i])
            left++;
        while (right > i && a[right] < a[i])
            right--;
        if (abs(i - left) < abs(i - right)) {
            for (int c = i; c - 1 >= left; c--) {
                ret++;
                swap(a[c], a[c - 1]);
            }
        }
        else {
            for (int c = i; c + 1 <= right; c++) {
                ret++;
                swap(a[c], a[c + 1]);
            }
        }
    }
    return ret;
}
*/

int dummy() {
    int ret = INF;

    int tmp[MAX];
    for (int i = 0; i < n; i++)
        tmp[i] = a[i];
    sort(tmp, tmp + n);

    do {
        int idx = 0;
        while (idx + 1 < n && tmp[idx] < tmp[idx + 1])
            idx++;
        while (idx + 1 < n && tmp[idx] > tmp[idx + 1])
            idx++;
        if (idx == n - 1) {
            ret = min(ret, calc(tmp));
        }
    } while (next_permutation(tmp, tmp + n));
    return ret;
}

int dyn[MAX];
int larger[MAX];

int recurse(int idx) {
    if (idx >= n)
        return 0;
    if (dyn[idx] != -1)
        return dyn[idx];
    
    int ans = INF;
    // Put it to the left of the largest
    ans = min(ans, recurse(idx + 1) + larger[idx]);
    // Put it to the right of the largest
    ans = min(ans, recurse(idx + 1) + (n - idx - 1 - larger[idx]));
    
    return dyn[idx] = ans;
}

void solveTest(int test) {
    fscanf(in, "%d", &n);
    for (int i = 0; i < n; i++)
        fscanf(in, "%d", &a[i]);
    
    int s[MAX];
    for (int i = 0; i < n; i++)
        s[i] = a[i];
    sort(s, s + n);
    for (int i = 0; i < n; i++) {
        int idx = 0;
        while (a[idx] != s[i])
            idx++;
        larger[i] = 0;
        for (int c = 0; c < idx; c++) {
            if (a[c] > s[i]) larger[i]++;
        }
    }
    
    memset(dyn, -1, sizeof(dyn));
    fprintf(out, "%d\n", recurse(0));
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("UpAndDown.in", "rt");
	out = fopen("UpAndDown.out", "wt");
	
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
