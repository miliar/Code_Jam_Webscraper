#include <algorithm>
#include <cstdio>
#include <vector>

#define REP(a, n) for (int a = 0; a<(n); ++a)

#define PB push_back
#define MP make_pair

using namespace std;

typedef pair<int, int> pii;

template<class T> inline int size(const T &t) { return t.size(); }

#define INF 1000000000

//////////////////////////////////////////


int byl[10], ile;

void parsuj(int M) {
    while (M) {
        if (!(byl[M%10]++))
            ++ile;
        M /= 10;
    }
}

int N;

void licz() {
    scanf("%d", &N);
    if (!N) {
        printf("INSOMNIA\n");
        return;
    }
    REP(a, 10)
        byl[a] = 0;
    ile = 0;
    for (int M = N; ; M += N) {
        parsuj(M);
        if (ile==10) {
            printf("%d\n", M);
            return;
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
