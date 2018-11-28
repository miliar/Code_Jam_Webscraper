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

const int inf = 1e9;
const int maxn = 10005;
const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, 1, -1, 0};

struct Elem
{
    int x, y, cnt;
    Elem(int _x, int _y, int _cnt) : x(_x), y(_y), cnt(_cnt) {} 
};

bool operator < (Elem first, Elem second)
{
    return first.cnt < second.cnt;
}

bool colored[maxn][maxn];
int k, n, m;

int get(int T)
{
    vector <Elem> list;
    forn(i, n)
        forn(j, m)
            colored[i][j] = ((i + j) % 2 == T);
    forn(i, n)
        forn(j, m)
        {
            int cnt = 0;
            forn(move, 4)
            {
                int x = i + dx[move];
                int y = j + dy[move];
                if (x >= 0 && x < n && y >= 0 && y < m && colored[x][y])
                    cnt++;
            }
 //           printf("%d %d %d\n", i, j, cnt);
            list.pb(Elem(i, j, cnt));
        }
    sort(list.begin(), list.end());

    map <pii, bool> got;
    forn(j, k)
    {
        //printf("get %d %d\n", list[j].x, list[j].y);
        got[mp(list[j].x, list[j].y)] = true;
    }
    int answer = 0;
    forn(j, k)
    {
        forn(move, 4)
        {
            int x = list[j].x + dx[move];
            int y = list[j].y + dy[move];
            if (got[mp(x, y)])
                answer++;
        }
    }
    return answer;
}

int main() {
#ifdef LOCAL
    freopen("inp", "r", stdin);
    //freopen("outp", "w", stdout);
#else
    // freopen(TASKNAME ".in", "r", stdin);
    // freopen(TASKNAME ".out", "w", stdout);
#endif
    int tests;
    scanf("%d", &tests);
    forn(test, tests)
    {
        scanf("%d%d%d", &n, &m, &k);
        int g1 = get(0);
        int g2 = get(1);
        int answer = min(g1, g2);
        printf("Case #%d: %d\n", test + 1, answer / 2);
    }
}
