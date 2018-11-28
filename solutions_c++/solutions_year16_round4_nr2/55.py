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

double pr[300];
int N, K;

double res[20][20];
double best;
int nr[20];

double czcz() {
    REP(a, N+1) REP(b, N+1)
        res[a][b] = 0;
    res[0][0] = 1;
    REP(a, K)
        REP(b, a+1) {
            res[a+1][b+1] += pr[nr[a]] * res[a][b];
            res[a+1][b] += (1 - pr[nr[a]]) * res[a][b];
        }
    return res[K][K/2];
}


void licz() {
    scanf("%d%d", &N, &K);
    REP(a, N)
        scanf("%lf", &pr[a]);
    best = 0;
    REP(x, 1<<N) {
        int z = 0;
        REP(a, N)
            if (x & (1 << a))
                nr[z++] = a;
        if (z == K)
            best = max(best, czcz());
    }
    printf("%.9f\n", best);
}

int main() {
    int T;
    scanf("%d", &T);
    REP(t, T) {
        printf("Case #%d: ", t+1);
        licz();
    }
}
