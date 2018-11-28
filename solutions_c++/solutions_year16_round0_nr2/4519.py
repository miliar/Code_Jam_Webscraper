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

int main() {
#ifdef YANAGI
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int testCount = NextInt();
    for (int testID = 1; testID <= testCount; ++testID) {
        string S = Next();
        while (S.size() > 0 && S[(int)S.size() - 1] == '+') S.erase((int)S.size() - 1, 1);
        S = S + "x";
        int res = 0;
        for (int i = 1; i < (int)S.size(); ++i) res += S[i] != S[i - 1];
        printf("Case #%d: %d\n", testID, res);
    }

    return 0;
}
