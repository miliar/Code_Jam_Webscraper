#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define INF 1e+9
#define mp make_pair
#define pb push_back
#define fi first
#define fs first
#define se second
#define i64 long long
#define li long long
#define lint long long
#define pii pair<int, int>
#define vi vector<int>

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, 1, -1, 0};
const int opp[4] = {3, 2, 1, 0};
const int maxn = 105;

#define DOWN 3
#define UP 0
#define LEFT 2
#define RIGHT 1

int cnt[maxn][maxn];
int n, m;
int a[maxn][maxn];
bool has_to[maxn][maxn];

void go(int x, int y, int move)
{
//    printf("go %d %d %d\n", x, y, move);
    while(true)
    {
        x += dx[move];
        y += dy[move];
        if (x > n || x == 0 || y > m || y == 0)
            return;
        if (a[x][y] != 4)
        {
            cnt[x][y]++;
            if (a[x][y] == opp[move])
                has_to[x][y] = true;
            return;
        }
        /*if (a[x][y] == opp[move])
        {
            cnt[x][y]++;
            printf("add %d %d\n", x, y);
            return;
        }
        else if (a[x][y] != 4)
            return;*/
    }
}

int main() {
#ifdef LOCAL
    //freopen("", "r", stdin);
    //freopen("outp", "w", stdout);
#else
    // freopen(TASKNAME ".in", "r", stdin);
    // freopen(TASKNAME ".out", "w", stdout);
#endif
    map<char, int> mm;
    mm['.'] = 4;
    mm['^'] = UP;
    mm['>'] = RIGHT;
    mm['v'] = DOWN;
    mm['<'] = LEFT;
    int tests;
    scanf("%d", &tests);
    forn(test, tests)
    {
        scanf("%d%d", &n, &m);
        fore(i, 1, n)
        {
            string s1;
            cin >> s1;
            fore(j, 1, m)
                a[i][j] = mm[s1[j - 1]];
        }
        memset(cnt, 0, sizeof(cnt));
        memset(has_to, 0, sizeof(has_to));
        fore(j, 1, m)
        {
            go(0, j, DOWN);
            go(n + 1, j, UP);
        }
        fore(i, 1, n)
        {
            go(i, 0, RIGHT);
            go(i, m + 1, LEFT);
        }
        bool fail = false;
        int answer = 0;
        fore(i, 1, n)
            fore(j, 1, m)
                if (cnt[i][j] == 4)
                {
                    fail = true;
                    break;
                }
                else if (has_to[i][j])
                    answer++;
        printf("Case #%d: ", test + 1);
        if (fail)
        {
            printf("IMPOSSIBLE\n");
        }
        else printf("%d\n", answer);

            
    }
}
