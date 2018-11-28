#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> II;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<II> VII;
typedef vector<string> VS;
typedef map<int, int> Map;
typedef set<int> Set;

inline string Next() {
    string S; cin >> S;
    return S;
}
inline string NextLine() {
    string S; getline(cin, S);
    return S;
}
inline int NextInt() {
    int n; scanf("%d", &n);
    return n;
}
inline LL NextLong() {
    LL n;
    #ifdef _WIN32
        scanf("%I64d", &n);
    #else
        scanf("%lld", &n);
    #endif
    return n;
}
inline double NextDouble() {
    double n; scanf("%lf", &n);
    return n;
}

const int N = 1 << 16;
int n, k;

bool IsPrime(LL n) {
    if (n <= 1) return false;
    for (LL i = 2; i * i <= n; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

int Factor(LL n) {
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) return i;
    }
}

int main() {
#ifdef YANAGI
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int testCount = NextInt();
    for (int testID = 1; testID <= testCount; ++testID) {
        n = NextInt();
        k = NextInt();
        printf("Case #%d: \n", testID);
        for (int tmask = 0; tmask < 1 << (n - 2); ++tmask) {
            int mask = (tmask << 1 | 1) | (1 << (n - 1));
            LL a[11];
            for (int p = 2; p <= 10; ++p) {
                a[p] = 0;
                for (int i = 0; i < n; ++i) a[p] = a[p] * p + (mask >> i & 1);
                assert(a[p] >= 0);
            }
            bool flag = true;
            for (int i = 2; i <= 10; ++i) {
                if (IsPrime(a[i])) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                for (int i = 0; i < n; ++i) printf("%d", mask >> i & 1); printf(" ");
                for (int i = 2; i <= 10; ++i) printf("%d ", Factor(a[i]));
                puts("");
                if (--k == 0) break;
            }
        }
    }

    return 0;
}
