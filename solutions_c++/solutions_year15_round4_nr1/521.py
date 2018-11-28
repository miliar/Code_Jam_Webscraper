#include <algorithm>
#include <array>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define rep(i,b) for(auto i=(0);i<(b);++i)
#define fo(i,a,b) for(auto i=(a);i<=(b);++i)
#define ford(i,a,b) for(auto i=(a);i>=(b);--i)
#define fore(a,b) for(auto a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }

int R, C;
char D[111][111];

ll res = 0;
bool no_res = false;

int DR[] = { 1, 0, -1, 0};
int DC[] = {0, 1, 0, -1};

bool check(int i, int j) {
    rep (d, 4) {
        int r = i, c = j;
        do {
            r += DR[d];
            c += DC[d];
            if (!(r >= 1 && r <= R && c >= 1 && c <= C))
                break;
            if (D[r][c] != '.')
                return 0;
        }
        while (r >= 1 && r <= R && c >= 1 && c <= C);
    }
    return true;
}

void go(int i, int j, int dr, int dc, char zn) {
    do {
        i += dr; j += dc;
        if (!(i >= 1 && i <= R && j >= 1 && j <= C))
            break;
        if (D[i][j] == '.') continue;
        if (D[i][j] != zn) {
            // do nothing
            return;
        }
        res += 1;
        if (check(i, j))
            no_res = true;
        break;
    } while (i >= 1 && i <= R && j >= 1 && j <= C);
}

void solve() {
    scanf("%d%d", &R, &C);
    res = 0;
    no_res = false;
    memset(D, 0, sizeof(D));
    fo (i, 1, R) fo (j, 1, C) scanf(" %c", &D[i][j]);

    fo (j, 1, C) {
        int i = 0;
        go(i, j, 1, 0, '^');
    }
    fo (j, 1, C) {
        int i = R + 1;
        go(i, j, -1, 0, 'v');
    }
    fo (i, 1, R) { int j = 0;
        go(i, j, 0, 1, '<');
    }
    fo (i, 1, R) { int j = C + 1;
        go(i, j, 0, -1, '>');
    }


    if (no_res)
        printf("IMPOSSIBLE\n");
    else
        printf("%lld\n", res);
}

int main(int argc, char ** argv) {
    ios::sync_with_stdio(false);

    //  freopen("../1.in","r",stdin);
    //  freopen("../2.in","r",stdin);
    //  freopen("../3.in","r",stdin);
    //  freopen("../A-small.in","r",stdin); freopen("../A-small.out","w",stdout);
    //  freopen("../A-small-attempt0.in","r",stdin);freopen("../A-small-attempt0.out","w",stdout);
    //  freopen("../A-small-attempt1.in","r",stdin);freopen("../A-small-attempt1.out","w",stdout);
    //  freopen("../A-small-attempt2.in","r",stdin);freopen("../A-small-attempt2.out","w",stdout);
    //  freopen("../A-large.in","r",stdin); freopen("../A-large.out","w",stdout);

    cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    int t;
    scanf("%d", &t);
    fo (i, 1, t) {
        printf("Case #%d: ", i);
        solve();
        fflush(stdout);
        cerr.flush();
    }
	return 0;
}
