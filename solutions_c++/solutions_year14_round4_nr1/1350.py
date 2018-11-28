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

int main() {
	FILE* fin = fopen("a.in", "r");
	FILE* fou = fopen("a.txt", "w");
	//fou = stdout;

	int T;
	fscanf(fin, "%d\n", &T);
	for (int C = 1; C <= T; C++) {
        int N, X, c;
        int S[20000];
        fscanf(fin, "%d %d", &N, &X);
        REP(i, N) {
            fscanf(fin, "%d", &S[i]);
        }
        sort(S, S + N);
        c = N;
        REP(i, N) {
            if (S[i] == -1)
                continue;
            FORD(j, N - 1, 0) {
                if (S[j] == -1 || i == j)
                    continue;
                if (S[i] + S[j] <= X) {
                    S[i] = S[j] = -1;
                    --c;
                    break;
                }
            }
        }
        fprintf(fou, "Case #%d: %d\n", C, c);
	}

	fclose(fin);
	fclose(fou);
}
