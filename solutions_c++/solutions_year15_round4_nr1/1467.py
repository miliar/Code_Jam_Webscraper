#include <bits/stdc++.h>
#define UN(v) sort(all(v)), (v).erase(unique(all(v)), (v).end())
#define FOR(i, a, b) for (int i(a), _B_##i(b); i < _B_##i; ++i)
#define CL(a, b) memset(a, b, sizeof a)
#define all(a) (a).begin(), (a).end()
#define REP(i, n) FOR(i, 0, n)
#define sz(a) int((a).size())
#define long int64_t
#define pb push_back
#define Y second
#define X first
#ifndef LOCAL
#define NDEBUG
#endif

using namespace std;

typedef pair<int, int> pii;

char line[1024];

int n, m;
char a[111][111];

bool good(int x, int y, int dx, int dy) {
    for (; ; ) {
        x += dx;
        y += dy;
        if (x < 0 || x >= m || y < 0 || y >= n)
            return false;
        if (a[y][x] != '.')
            return true;
    }
}

int main() {
    for (int tc = 0, T = atoi(gets(line)); tc++ < T; ) {
        gets(line);
        sscanf(line, "%d%d", &n, &m);
        REP (i, n) gets(a[i]);
        int res = 0;
        REP (i, n) REP (j, m) {
            if (res < 0)
                break;
            if (a[i][j] == '.')
                continue;
            int x = i, y = j, dx = 0, dy = 0;
            switch (a[i][j]) {
                case '<': dx = -1; break;
                case '>': dx = +1; break;
                case '^': dy = -1; break;
                case 'v': dy = +1; break;
            }
            if (good(j, i, dx, dy))
                continue;
            if (good(j, i, -1, 0)) {
                a[i][j] = '<';
                ++res;
                continue;
            }
            if (good(j, i, +1, 0)) {
                a[i][j] = '>';
                ++res;
                continue;
            }
            if (good(j, i, 0, -1)) {
                a[i][j] = '^';
                ++res;
                continue;
            }
            if (good(j, i, 0, +1)) {
                a[i][j] = 'v';
                ++res;
                continue;
            }
            res = -1;
        }
        printf("Case #%d: ", tc);
        if (res < 0)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", res);
    }
    return 0;
}
