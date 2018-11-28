#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <list>
#include <cstdlib>
#include <cstdio>
#include <string>
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

unsigned int a[2000];

int N;

struct node {
    unsigned int v;
    int i;
};
node ma[2000];

int distance() {
    int rev = 0;
    int t[1200];
    for (int i = 0; i < N; i++) {
        t[ma[a[i]].i] = i;
    }
    for (int i = 0; i < N - 1; i++) {
        for (int j = i + 1; j < N; j++)
            if (t[i] > t[j])
                rev++;
    }
    return rev;
}

int solve(int d, int l, int r) {
    if (d == N - 1) {
        // find the distance!
        a[l] = d;
        return distance();
    }
    int m;
    a[l] = d;
    m = solve(d + 1, l + 1, r);
    a[r] = d;
    m = min(m, solve(d + 1, l, r - 1));
    return m;
}

bool node_cmp(const node &x, const node&y) {
    return x.v < y.v;
}

int main() {
	FILE* fin = fopen("a.in", "r");
	FILE* fou = fopen("a.txt", "w");
	//fou = stdout;

	int T;
	fscanf(fin, "%d\n", &T);
	for (int C = 1; C <= T; C++) {
        fscanf(fin, "%d", &N);
        REP(i, N) {
            fscanf(fin, "%d", &ma[i].v);
            ma[i].i = i;
        }

        sort(ma, ma + N, node_cmp);
        fprintf(fou, "Case #%d: %d\n", C, solve(0, 0, N - 1));
	}

	fclose(fin);
	fclose(fou);
}
