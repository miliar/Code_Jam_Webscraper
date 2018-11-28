#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>

#define REP(a, n) for (int a = 0; a<(n); ++a)

#define PB push_back
#define MP make_pair

using namespace std;

typedef pair<int, int> pii;

template<class T> inline int size(const T &t) { return t.size(); }

#define INF 1000000000

//////////////////////////////////////////

int N;
char tab[100][100];
bool byl[2][100];

void dfs(int a, int b, int &s1, int &s2) {
    if (byl[a][b])
        return;
    byl[a][b] = 1;
    if (!a) ++s1; else ++s2;
    REP(b2, N)
        if ((!a ? tab[b][b2] : tab[b2][b]) == '1')
            dfs(1 - a, b2, s1, s2);
}

vector<pii> grupy;
int best = INF;
int ile10, ile01;

void rec(int n, vector<pii> &g2) {
    if (n == size(grupy)) {
        int r = 0;
        int p10 = 0, p01 = 0;
        REP(a, size(g2)) {
            int r1 = g2[a].first, r2 = g2[a].second;
            if (r1 < r2)
                p10 += r2 - r1;
            else
                p01 += r1 - r2;
            r += max(r1, r2) * max(r1, r2);
        }
        if (p10 > ile10 || p01 > ile01)
            return;
        r += ile10 - p10;
        best = min(best, r);
        return;
    }
    g2.PB(grupy[n]);
    rec(n + 1, g2);
    g2.pop_back();
    REP(a, size(g2)) {
        g2[a].first += grupy[n].first;
        g2[a].second += grupy[n].second;
        rec(n + 1, g2);
        g2[a].first -= grupy[n].first;
        g2[a].second -= grupy[n].second;
    }
}

void licz() {
    grupy.clear();
    best = INF;
    int bylo = 0;
    scanf("%d", &N);
    REP(y, N) {
        scanf("%s", tab[y]);
        REP(x, N)
            if (tab[y][x] == '1')
                ++bylo;
    }
    REP(a, 2) REP(b, N)
        byl[a][b] = 0;
    ile10 = ile01 = 0;
    REP(a, 2) REP(b, N)
        if (!byl[a][b]) {
            int s1 = 0, s2 = 0;
            dfs(a, b, s1, s2);
            if (s1 == s2)
                bylo -= s1 * s2;
            else if (s1 == 1 && s2 == 0)
                ++ile10;
            else if (s1 == 0 && s2 == 1)
                ++ile01;
            else
                grupy.PB(MP(s1, s2));
//            printf("\n%d %d\n", s1, s2);
        }
    vector<pii> g2;
    rec(0, g2);
    printf("%d\n", best - bylo);
    fprintf(stderr, "%d\n", best - bylo);
}

int main() {
    int T;
    scanf("%d", &T);
    REP(t, T) {
        printf("Case #%d: ", t+1);
        fprintf(stderr, "Case #%d: ", t+1);
        licz();
    }
}
