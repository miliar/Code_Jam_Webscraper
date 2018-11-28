#include <algorithm>
#include <cstdio>
#include <vector>

#define REP(a, n) for (int a = 0; a<(n); ++a)
#define FOR(a, b, c) for (int a = (b); a<=(c); ++a)

#define PB push_back
#define MP make_pair

using namespace std;

typedef pair<int, int> pii;
typedef long long LL;

template<class T> inline int size(const T &t) { return t.size(); }

#define INF 1000000000

//////////////////////////////////////////

#define TOP 0
#define BOT 1
#define LEFT 2
#define RIGHT 3

char tab[100][101];
int YS, XS;

void change(int &x, int &y, int &c, int nr, int cel) {
    if (nr < XS) {
        y = 0 - cel; 
        x = nr;
        c = TOP;
    }
    else if (nr < XS + YS) {
        y = nr - XS;
        x = XS - 1 + cel;
        c = RIGHT;
    }
    else if (nr < XS + YS + XS) {
        y = YS - 1 + cel;
        x = XS - 1 - (nr - XS - YS);
        c = BOT;
    }
    else {
        y = YS - 1 - (nr - XS - YS - XS);
        x = 0 - cel;
        c = LEFT;
    }
}

bool polacz(int start, int meta) {
    int x, y, c, xr, yr, cr;
    change(x, y, c, start, 0);
    change(xr, yr, cr, meta, 1);
    for (;;) {
        char &r = tab[y][x];
        if (r == ' ')
            r = (c == TOP || c == BOT) ? '\\' : '/';
        if (c == TOP) {
            if (r == '\\') {
                ++x;
                c = LEFT;
            }
            else {
                --x;
                c = RIGHT;
            }
        }
        else if (c == RIGHT) {
            if (r == '\\') {
                --y;
                c = BOT;
            }
            else {
                ++y;
                c = TOP;
            }
        }
        else if (c == BOT) {
            if (r == '\\') {
                --x;
                c = RIGHT;
            }
            else {
                ++x;
                c = LEFT;
            }
        }
        else if (c == LEFT) {
            if (r == '\\') {
                ++y;
                c = TOP;
            }
            else {
                --y;
                c = BOT;
            }
        }
        if (x < 0 || y < 0 || x >= XS || y >= YS)
            return x == xr && y == yr;
    }
}


int pary[400];

bool licz() {
    scanf("%d%d", &YS, &XS);
    REP(p, XS+YS) {
        int a, b;
        scanf("%d%d", &a, &b);
        --a; --b;
        pary[a] = b;
        pary[b] = a;
    }
    REP(y, YS) {
        REP(x, XS) 
            tab[y][x] = ' ';
        tab[y][XS] = 0;
    }
    REP(a, 2*XS+2*YS) {
        if (pary[a] < a)
            if (!polacz(pary[a], a))
                return 0;
    }
    REP(y, YS) {
        REP(x, XS)
            if (tab[y][x] == ' ')
                tab[y][x] = '/';
        printf("%s\n", tab[y]);
    }
    return 1;
}

int main() {
    int T;
    scanf("%d", &T);
    REP(t, T) {
        printf("Case #%d:\n", t+1);
        if (!licz())
            printf("IMPOSSIBLE\n");
    }
}
