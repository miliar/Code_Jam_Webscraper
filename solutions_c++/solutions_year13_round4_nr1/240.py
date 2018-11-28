#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>

#define REP(AA,BB) for(int AA=0; AA<(BB); ++AA)
#define FOR(AA,BB,CC) for(int AA=(BB); AA<(CC); ++AA)
#define FC(AA,BB) for(__typeof((AA).begin()) BB=(AA).begin(); BB!=(AA).end(); ++BB)
#define SZ(AA) ((int)((AA).size()))
#define ALL(AA) (AA).begin(), (AA).end()
#define PB push_back
#define MP make_pair

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;
typedef long double LD;

struct pod {
    int a, v, c;
    pod (int _a = 0, int _v = 0, int _c = 0)
        : a(_a), v(_v), c(_c) {}
    int operator<(const pod &p) const {
        if (a == p.a) {
            return v < p.v;
        }
        return a < p.a;
    }
};

const int MOD = 1000002013;

int cost(int a, int b, int N, int p) {
    int delta = b - a;
    LL res = ((LL)N * delta) % MOD;
    LL tmp = ((LL)delta * (delta - 1) / 2) % MOD;
    res = (res + MOD - tmp) % MOD;
    res = (res * p) % MOD;
    return (int)res;
}

int main(void) {
    int T; scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        priority_queue<PII> PQ;
        vector<pod> P;
        int N, M; scanf("%d%d", &N, &M);
        LL net = 0;
        REP (i, M) {
            int a, b, c; scanf("%d%d%d", &a, &b, &c);
            P.PB(pod(a, -1, c));
            P.PB(pod(b, 1, c));
            net = (net + cost(a, b, N, c)) % MOD;
        }
        sort(ALL(P));
        FC (P, it) {
            pod p = *it;
            if (p.v == -1) {
                PQ.push(MP(p.a, p.c));
            } else {
                while (p.c > 0) {
                    PII t = PQ.top(); PQ.pop();
                    int mn = min(p.c, t.second);
                    net = (net + MOD - cost(t.first, p.a, N, mn)) % MOD;
                    p.c -= mn;
                    t.second -= mn;
                    if (t.second > 0) {
                        PQ.push(t);
                    }
                }
            }
        }
        printf("Case #%d: %Ld\n", test, net);
    }
    return 0;
}

