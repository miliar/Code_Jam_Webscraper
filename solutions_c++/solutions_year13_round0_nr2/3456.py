#include <cstdio>
#include <vector>
using namespace std;

const int MAXN = 110;
const int MAXA = 110;
int lawn[MAXN][MAXN];
vector< pair<int,int> > vpos[MAXA];

bool solve()
{
    int n, m;
    for (int i = 0; i < MAXA; ++i)
        vpos[i].clear();
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            scanf("%d", lawn[i] + j);
            vpos[lawn[i][j]].push_back(make_pair(i, j));
        }
    }

    for (int q = 0; q < MAXA; ++q) {
        for (auto it = vpos[q].begin(); it != vpos[q].end(); ++it) {
            bool colok = true, rowok = true;
            // check col
            for (int i = 0; i < n; ++i) {
                if (lawn[i][it->second] > lawn[it->first][it->second])
                    colok = false;
            }
            // check row
            for (int i = 0; i < m; ++i) {
                if (lawn[it->first][i] > lawn[it->first][it->second])
                    rowok = false;
            }
            if (!colok && !rowok)
                return false;

            if (colok)
                for (int i = 0; i < n; ++i)
                    lawn[i][it->second] = -1;

            if (rowok)
                for (int i = 0; i < m; ++i)
                    lawn[it->first][i] = -1;

        }
    }
    return true;
}


int main()
{
    int tst;
    scanf("%d", &tst);
    for (int i = 0; i < tst; ++i) {
        printf("Case #%d: %s\n", i+1, solve() ? "YES" : "NO");
    }
}
