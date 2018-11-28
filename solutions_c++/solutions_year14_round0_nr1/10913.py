#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define SZ(v) ((int)(v).size())
#define FOR(i, a, b) for (typeof(a) i = (a); i < (b); ++i)
#define FORD(i, a, b) for(typeof(a) i = (a);i >= (b); --i)
#define FOREACH(iter, v) for (typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define REP(i, n) FOR(i, 0, n)

using namespace std;

#define SMALL 1

int main()
{

#if SMALL
    freopen("A-small.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
#else
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif

    int tc;
    int grid[4][4], grid2[4][4];

    scanf("%d", &tc);
    int row1, row2;
    for (int t = 1; t <= tc; ++t) {
        int a[4], b[4];
        scanf("%d", &row1);
        REP(i,4) REP(j,4) scanf("%d", &grid[i][j]);
        REP(i,4) a[i] = grid[row1-1][i];
        scanf("%d", &row2);
        REP(i,4) REP(j,4) scanf("%d", &grid2[i][j]);
        REP(i,4) b[i] = grid2[row2-1][i];
        vector<int> ans;
        REP(i,4) REP(j,4) {
            if (a[i] == b[j]) ans.push_back(a[i]);
        }
        int num = SZ(ans);
        printf("Case #%d: ", t);
        if (num == 1) printf("%d\n", ans[0]);
        else if (num > 1) printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");
    }

	return 0;
}
