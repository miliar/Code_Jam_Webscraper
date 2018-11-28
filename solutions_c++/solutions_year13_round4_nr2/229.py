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

LL worst(int n, LL p) {
    if ((1LL << n) - 1 == p) {
        return p + 1;
    }
    int last = -1;
    for (int i = 0; i < n; ++i) {
        if ((1LL << n) - (1LL << (n - i)) <= p) {
            last = i;
        } else {
            break;
        }
    }
    return (1LL << (last + 1)) - 1;
}

LL best(int n, LL p) {
    int last = -1;
    for (int i = 0; i <= n; ++i) {
        if ((1LL << (n - i)) - 1 <= p) {
            last = i;
            break;
        }
    }
    return (1LL << n) - (1LL << last);
}

int main(void) {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int n; LL p;
        scanf("%d%lld", &n, &p);
        --p;
        printf("Case #%d: %lld %lld\n", t, worst(n, p) - 1, best(n, p));
    }
    return 0;
}

