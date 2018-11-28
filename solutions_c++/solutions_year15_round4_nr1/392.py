#include <bits/stdc++.h>

using namespace std;

#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
#define forab(i,a,b) for (int i = int(a); i < int(b); ++i)

typedef long long ll;
typedef long double ld;

const int INF = 1000001000;
const ll INFL = 2000000000000001000;
int solve();


int main()
{
    srand(2317);
    cout.precision(10);
    cout.setf(ios::fixed);
    #ifdef LOCAL
    freopen("a.in", "r", stdin);
    #else
    #endif
    int tn = 1;
    cin >> tn;
    for (int i = 0; i < tn; ++i)
        solve();
    #ifdef LOCAL
    cerr << "Time: " << double(clock()) / CLOCKS_PER_SEC << '\n';
    #endif
}

int test = 1;

const int maxn = 200;

string s[maxn];
int chtodir[1000];

const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, -1, 0, 1};

int solve()
{
    chtodir[int('^')] = 0;
    chtodir[int('<')] = 1;
    chtodir[int('v')] = 2;
    chtodir[int('>')] = 3;
    int n, m;
    cin >> n >> m;
    forn (i, n)
        cin >> s[i];
    int ans = 0;
    forn (i, n)
        forn (j, m)
        {
            if (s[i][j] == '.')
                continue;
            int dir = chtodir[int(s[i][j])];
            int x = i, y = j;
            x += dx[dir], y += dy[dir];
            while (x >= 0 && x < n && y >= 0 && y < m && s[x][y] == '.')
                x += dx[dir], y += dy[dir];
            if (x >= 0 && x < n && y >= 0 && y < m)
                continue;
            bool fail = true;
            forn (dir, 4)
            {
                int x = i, y = j;
                x += dx[dir], y += dy[dir];
                while (x >= 0 && x < n && y >= 0 && y < m && s[x][y] == '.')
                    x += dx[dir], y += dy[dir];
                if (x >= 0 && x < n && y >= 0 && y < m)
                {
                    fail = false;
                    break;
                }
            }
            if (fail)
                ans = -INF;
            ++ans;
        }
    if (ans < 0)
        printf("Case #%d: IMPOSSIBLE\n", test++);
    else
        printf("Case #%d: %d\n", test++, ans);
    return 0;
}
