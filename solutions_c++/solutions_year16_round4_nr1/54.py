#include <algorithm>
#include <cstdio>
#include <vector>

#define REP(a, n) for (int a = 0; a<(n); ++a)
#define FORD(a, b, c) for (int a = (b); a>=(c); --a)

#define PB push_back
#define MP make_pair

using namespace std;

typedef pair<int, int> pii;

template<class T> inline int size(const T &t) { return t.size(); }

#define INF 1000000000

//////////////////////////////////////////
int N, R, P, S, len;

char tab[10];

char wins(char a, char b) {
    if ((a == 'P' && b == 'R') || (a == 'R' && b == 'P'))
        return 'P';
    if ((a == 'S' && b == 'R') || (a == 'R' && b == 'S'))
        return 'R';
    return 'S';
}

bool check() {
    int ile[3];
    REP(a, 3) ile[a] = 0;
    REP(a, len)
        ++ile[tab[a] == 'P' ? 0 : tab[a] == 'R' ? 1 : 2];
    if (ile[0] != P || ile[1] != R)
        return 0;
    char t2[10];
    REP(a, len)
        t2[a] = tab[a];
    int l2 = len;
    while (l2 > 1) {
        int a = 0, b = 0;
        while (a < l2) {
            if (t2[a] == t2[a + 1])
                return 0;
            t2[b++] = wins(t2[a], t2[a + 1]);
            a += 2;
        }
        l2 /= 2;
    }
    return 1;
}

void licz() {
    scanf("%d%d%d%d", &N, &R, &P, &S);
    len = 1 << N;
    tab[len] = 0;
    REP(a, len)
        tab[a] = 'P';
    for (;;) {
        if (check()) {
            printf("%s\n", tab);
            break;
        }
        bool ok = 0;
        FORD(a, len - 1, 0) {
            if (tab[a] == 'S') {
                tab[a] = 'P';
                continue;
            } else {
                tab[a] = (tab[a] == 'P') ? 'R' : 'S';
                ok = 1;
                break;
            }
        }
        if (!ok) {
            printf("IMPOSSIBLE\n");
            break;
        }
    }
}

int main() {
    int T;
    scanf("%d", &T);
    REP(t, T) {
        printf("Case #%d: ", t+1);
        licz();
    }
}
