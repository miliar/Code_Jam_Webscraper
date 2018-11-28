#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <list>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <map>
#include <queue>

using namespace std;

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define ALL(c) (c).begin(), (c).end()
#define VAR(v, i) __typeof(i) v = (i)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back

#define I64d "%I64d"
#define I64u "%I64u"

void disp(vector<int>& arr, int sum=0) {
    for (vector<int>::iterator it = arr.begin(); it != arr.end(); ++it)
        printf("<%d>", *it);
    printf("\n");
    int x = arr.front();
    FOREACH(it, arr) {
        sum -= *it;
    }
    if (sum != 0)
        printf("WA");
}

int main() {
	FILE* fin = fopen("a.in", "r");
	FILE* fou = fopen("a.txt", "w");
	//fou = stdout;

	int T;
	fscanf(fin, "%d\n", &T);
	for (int C = 1; C <= T; C++) {
        int n;
        int best, now;
        fscanf(fin, "%d", &n);
        vector<int> arr;
        REP(i, n) {
            int x;
            fscanf(fin, "%d", &x);
            arr.PB(x);
        }
        sort(ALL(arr));
        reverse(ALL(arr));
        best = arr.front();
        for (int sz = 2, msz = arr.front(); sz < msz; ++sz) {
            int sum = sz;
            FOREACH(it, arr) {
                sum += (*it + sz - 1) / sz - 1;
            }
            best = min(sum, best);
        }

        fprintf(fou, "Case #%d: %d\n", C, best);
	}

	fclose(fin);
	fclose(fou);
}
