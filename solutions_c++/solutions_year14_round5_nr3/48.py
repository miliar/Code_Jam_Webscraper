#include <cstdio>
#include <algorithm>
#include <map>

using namespace std;

int n, mn;
char tip[1100][5];
int who[1100];
int bio[20][1<<15][32];
int cookie, cnt;
map<int,int> M;

void rec (int x, int mask, int inside) {
//    printf ("%d %d %d\n", x, mask, inside);
    if (x == n) {
        mn = min(mn, __builtin_popcount(mask) + inside);
        return;
    }

    int &ref = bio[x][mask][inside];
    if (ref == cookie) return;
    ref = cookie;

    if (tip[x][0] == 'E') {
        if (who[x] != 0) {
            int w = M[who[x]];
            if (mask & (1 << w)) return;
            rec (x + 1, mask | (1 << w), inside);
        }
        else {
            for (int i = 0; i < (int)M.size(); ++i)
                if ((mask & (1 << i)) == 0)
                    rec (x + 1, mask | (1 << i), inside);
            rec (x + 1, mask, inside + 1);
        }
    }
    else {
        if (who[x] != 0) {
            int w = M[who[x]];
            if (mask & (1 << w)) rec (x + 1, mask ^ (1 << w), inside);
        }
        else {
            for (int i = 0; i < (int)M.size(); ++i)
                if (mask & (1 << i))
                    rec (x + 1, mask ^ (1 << i), inside);
            if (inside) rec (x + 1, mask, inside - 1);
        }
    }
}

void solve ()
{
    scanf ("%d", &n);

    M.clear();
    cnt = 0;

    for (int i = 0; i < n; ++i) {
        scanf ("%s%d", tip[i], who+i);
        if (who[i] && M.count(who[i]) == 0) 
            M[who[i]] = cnt++;
    }

    mn = 1e9;
    ++cookie;

    for (int i = 0; i <= 15; ++i)
        for (int j = 0; j < (1 << M.size()); ++j)
            rec (0, j, i);

    if (mn == 1e9) printf ("CRIME TIME\n");
    else printf ("%d\n", mn);
}

int main (int argc, char *argv[])
{
    int No; scanf ("%d", &No);
    for (int i = 0; i < No; ++i) {
        if (argc == 1) printf ("Case #%d: ", i + 1);
        solve();
    }

    return 0;
}


