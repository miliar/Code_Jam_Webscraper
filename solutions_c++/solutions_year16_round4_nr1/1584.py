#include <iostream>
#include <vector>
#include <map>
#include <functional>
#include <string>
#include <memory>
#include <cstring>
#include <climits>
#include <cassert>
#include <algorithm>
#include <cstdio>
#include <set>
#include <cstdlib>

using namespace std;

#define REP(i, n) for (int (i) = 0; (i) < (n); ++i)
#define FOR(i, a, b) for (int (i) = (a); (i) <= (b); ++i)
#define FORD(i, a, b) for (int (i) = (a); (i) >= (b); --i)
#define ALL(a) (a).begin(), (a).end()
#define SIZE(a) (int)((a).size())

#define DBG(x) cout << #x << " = " << (x) << '\n'

typedef vector<int> VI;
typedef long long LL;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

char play(char c, char c2) {
    if (c > c2) swap(c, c2);
    if (c == 'P' && c2 == 'R') return 'P';
    if (c == 'P' && c2 == 'S') return 'S';
    if (c == 'R' && c2 == 'S') return 'R';
    return '-';
}

bool check(const string &s) {
    int n = SIZE(s);
    if (n == 1) return true;
    string a;
    for (int i = 0; i < n; i += 2) {
        char c = s[i];
        char c2 = s[i + 1];
        if (c == c2) return false;
        a += play(c, c2);
    }
    return check(a);
}

string doit(int R, int P, int S) {
    string s = string(P, 'P') + string(R, 'R') + string(S, 'S');

    for(;;) {
        if (check(s)) return s;
        if (!next_permutation(ALL(s))) return "IMPOSSIBLE";
    }

    return "";
}

int main()
{
    int T;
    cin >> T;
    REP(zzz, T) {
        int N, R, P, S;
        cin >> N >> R >> P >> S;
        cout << "Case #" << zzz + 1 << ": " << doit(R, P, S) << '\n';
    }

    return 0;
}

/*
int main() {
    int T;
    scanf("%d", &T);
    REP(zzz, T) {
        int K, C, S;
        scanf("%d %d %d", &K, &C, &S);
        printf("Case #%d:", zzz + 1);
        doit(K, C, S);
        printf("\n");
    }

    return 0;
}
*/
