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

int main() {
	FILE* fin = fopen("a.in", "r");
	FILE* fou = fopen("a.txt", "w");
	//fou = stdout;

	int T;
	fscanf(fin, "%d\n", &T);
	for (int C = 1; C <= T; C++) {
        int n, realcnt = 0, cnt = 0;

        fscanf(fin, "%d ", &n);
        for (int i = 0; i <= n; ++i) {
            char x;
            int t;
            fscanf(fin, "%c", &x);
            t = x - '0';
            realcnt += t;
            cnt = (cnt < i) ? i + t : cnt + t;
        }
        fprintf(fou, "Case #%d: %d\n", C, cnt - realcnt);
	}

	fclose(fin);
	fclose(fou);
}
