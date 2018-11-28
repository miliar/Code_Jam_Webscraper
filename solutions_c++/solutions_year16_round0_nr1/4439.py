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
    LL n; scanf("%lld", &n);
    return n;
}
inline double NextDouble() {
    double n; scanf("%lf", &n);
    return n;
}

int main() {
#ifdef YANAGI
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int testCount = NextInt();
    for (int testID = 1; testID <= testCount; ++testID) {
        int n = NextInt();
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", testID);
            continue;
        }
        int mask = 0;
        for (int k = 1; k <= 100000; ++k) {
            LL t = (LL)n * k;
            while (t > 0) {
                mask |= (1 << (t % 10));
                t /= 10;
            }
            if (mask == 1023) {
                printf("Case #%d: %lld\n", testID, k * LL(n));
                break;
            }
        }
    }

    return 0;
}
