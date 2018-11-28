#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string.h>
#include <queue>
#include <cstdio>
#include <cassert>
#include <deque>
#include <stack>
#include <utility>
#include <numeric>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

struct Edge {
    int v, id;
    Edge() {}
    Edge(int v, int id) : v(v), id(id) {}
};

const int MAXN = 82;

int n;
vector<int> cost;
vector< vector<Edge> > g;
vector<int> p;
vector<int> pe;
bool vp[MAXN][MAXN][MAXN];
bool ep[MAXN][MAXN][MAXN];

void dfs(int v, int pr) {
    p[v] = pr;
    forv(i, g[v]) {
        int u = g[v][i].v;
        if (u != pr) {
            pe[u] = g[v][i].id;
            dfs(u, v);
        }
    }
}

int dp[2][2][2][MAXN][MAXN][MAXN][MAXN];

int calc(char who, char s1, char c1, char s2, char c2, char st1, char st2) {
    int& res = dp[st1][st2][who][s1][c1][s2][c2];
    if (res != -1) return res;
	if (st1 && st2) return 0;
	res = -1e9;
    if (who == 0) {
		if (st1) return -calc(who ^ 1, s1, c1, s2, c2, st1, st2);
		bool hasMove = false;
        int add = 0;
        if ((c1 == c2 && !st2) || !vp[s2][c2][c1]) add += cost[c1];
        forv(i, g[c1]) {
            int eid = g[c1][i].id;
            if (ep[s1][c1][eid] || ep[s2][c2][eid]) continue;
            int vid = g[c1][i].v;
            //if (vp[s1][c1][vid]) continue;
			//if (!vp[s2][c2][vid] || vid == c2) {
				hasMove = true;
				res = max(res, add - calc(who ^ 1, s1, vid, s2, c2, st1, st2));
			//}
        }
		if (!hasMove) {
			res = add - calc(who ^ 1, s1, c1, s2, c2, 1, st2);
		}
    } else {
		if (st2) return -calc(who ^ 1, s1, c1, s2, c2, st1, st2);
        int add = 0;
		bool hasMove = false;
        if ((c1 == c2 && !st1) || !vp[s1][c1][c2]) add += cost[c2];
        forv(i, g[c2]) {
            int eid = g[c2][i].id;
            if (ep[s1][c1][eid] || ep[s2][c2][eid]) continue;
            int vid = g[c2][i].v;
            //if (vp[s2][c2][vid]) continue;
			//if (!vp[s1][c1][vid] || vid == c1) {
				hasMove = true;
				res = max(res, add - calc(who ^ 1, s1, c1, s2, vid, st1, 0));
			//}
        }      
		if (!hasMove) {
			res = add - calc(who ^ 1, s1, c1, s2, c2, st1, 1);
		}
    }
    return res;
}

void solve(int tc) {
    cerr << "Case #" << tc << ", " << clock() << " ms.\n";
    cout << "Case #" << tc << ": ";
    cin >> n;
    cost = vector<int>(n);
    forn(i, n) cin >> cost[i];
    g = vector< vector<Edge> >(n);
    forn(i, n - 1) {
        int j;
        cin >> j;
        j--;
        g[i].pb(Edge(j, i));
        g[j].pb(Edge(i, i));
    }
    p = vector<int>(n);
    pe = vector<int>(n);
    memset(vp, 0, sizeof(vp));
    memset(ep, 0, sizeof(ep));
    forn(i, n) {
        dfs(i, -1);
        forn(j, n) {
            int v = j;
            while (v != i) {
                vp[i][j][v] = true;
                ep[i][j][pe[v]] = true;
                v = p[v];    
            }
            vp[i][j][v] = true;
        }        
    }
    memset(dp, 255, sizeof(dp));
    int ans = -1e9;
    forn(i, n) {
        int cur = 1e9;
        forn(j, n) {
            int val = calc(0, i, i, j, j, 0, 0);
            cur = min(cur, val);
        }     
        ans = max(ans, cur);
		//cerr << i << " " << ans << endl;
    }   
    cout << ans << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    forn(i, tc) solve(i + 1);
    return 0;
}
