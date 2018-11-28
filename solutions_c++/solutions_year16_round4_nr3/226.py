
#include <bits/stdc++.h>

#define FOR(i,b,e) for(int i=(b); i <= (e); ++i)
#define FORD(i,b,e) for(int i=(b); i >= (e); --i)
#define SIZE(c) (int) (c).size()
#define FORE(i,c) FOR(i,0,SIZE(c)-1)
#define FORDE(i,c) FORD(i,SIZE(c)-1,0)
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

using namespace std;

typedef long long int LLI;
typedef pair < int , int > PII;
typedef pair < LLI , LLI > PLL;

typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < PII > VP;
typedef vector < LLI > VL;
typedef vector < PLL > VPL;

typedef vector < VI > VVI;
typedef vector < VL > VVL;
typedef vector < VB > VVB;
typedef vector < VP > VVP;

const int MOD = 1000000007;
const int INF = 1000000001;
const LLI LLINF = 1000000000000000001LL;

/*************************************************************************/

int id(int i, int j, int n, int m, int side) {
    return 4 * (i * m + j) + side;
}

int getVert(int num, int r, int c) {
    int i, j, side;

    if (num <= c) {
        i = 0;
        j = num - 1;
        side = 2;
    } else if (num <= c + r) {
        i = num - c - 1;
        j = c - 1;
        side = 1;
    } else if (num <= 2 * c + r) {
        i = r - 1;
        j = (c - 1) - (num - c - r - 1);
        side = 0;
    } else {
        i = (r - 1) - (num - 2 * c - r - 1);
        j = 0;
        side = 3;
    }

    return id(i, j, r, c, side);
}

bool conn(int a, int b, VVI &tab) {
    int n = SIZE(tab), m = SIZE(tab[0]);
    int v = 4 * n * m;

    VVI graph(v);

    int dx[] = {1, 0, -1, 0};
    int dy[] = {0, 1, 0, -1};

    FOR(i,0,n-1) FOR(j,0,m-1) FOR(d,0,1) {
        int ip = i + dx[d];
        int jp = j + dy[d]; // lol

        if (ip >= 0 && ip < n && jp >= 0 && jp < m) {
            int dp = d + 2;
            int ids[] = {
                id(i, j, n, m, d),
                id(ip, jp, n, m, dp)
            };

            graph[ids[0]].PB(ids[1]);
            graph[ids[1]].PB(ids[0]);
        }
    }

    FOR(i,0,n-1) FOR(j,0,m-1) {
        vector <int> sides;

        if (tab[i][j]) {
            sides = {1,2,0,3};
        } else {
            sides = {1,0,2,3};
        }

        int ids[4];

        FOR(it,0,3) {
            ids[it] = id(i, j, n, m, sides[it]);
        };

        for (int it = 0; it <= 2; it += 2) {
            graph[ids[it]].PB(ids[it+1]);
            graph[ids[it+1]].PB(ids[it]);
        }
    }

    int src = getVert(a, n, m);
    int dest = getVert(b, n, m);

    queue <int> q;
    q.push(src);

    VB seen(v,false);
    seen[src] = true;

    while (!q.empty()) {
        int top = q.front();
        q.pop();

        if (top == dest) return true;

        for (int x : graph[top]) if (!seen[x]) {
            seen[x] = true;
            q.push(x);
        }
    }

    return false;
}

int main() {
    ios_base::sync_with_stdio(0);

    int t;
    cin >> t;

    FOR(i,1,t) {
        int r, c;
        cin >> r >> c;

        int m = r * c;
        int k = 2 * (r + c);

        VI perm(k);
        FOR(j,0,k-1) cin >> perm[j];

        int M = (1 << m);
        VVI ans;

        FOR(mask,0,M-1) {
            VVI tab(r, VI(c));
            FOR(i,0,r-1) FOR(j,0,c-1) {
                int id = i * c + j;

                if (mask & (1 << id)) tab[i][j] = 1;
                else tab[i][j] = 0;
            }

            bool good = true;
            for (int j = 0; j < k; j += 2) {
                if (!conn(perm[j], perm[j+1], tab)) {
                    good = false;
                    break;
                }
            }

            if (good) {
                ans = tab;
                break;
            }
        }

        cout << "Case #" << i << ": \n";

        if (ans.empty()) {
            cout << "IMPOSSIBLE\n";
        } else {
            FOR(i,0,r-1) {
                FOR(j,0,c-1) cout << (ans[i][j] ? "\\" : "/");
                cout << '\n';
            }
        }
    }

    return 0;
}

/*************************************************************************/

