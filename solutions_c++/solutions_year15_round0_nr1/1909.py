#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define INF 1e+9
#define mp make_pair
#define pb push_back
#define fi first
#define fs first
#define se second
#define i64 long long
#define li long long
#define lint long long
#define pii pair<int, int>
#define vi vector<int>

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)

int main() {
#ifdef LOCAL
    freopen("inp", "r", stdin);
    freopen("outp", "w", stdout);
#else
    // freopen(TASKNAME ".in", "r", stdin);
    // freopen(TASKNAME ".out", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    forn(test, T)
    {
        int n;
        string s;
        scanf("%d", &n);
        cin >> s;
        int sum = 0;
        int ans = 0;
        forn(pos, n + 1)
        {
            int x = s[pos] - '0';
            if (sum < pos)
            {
                ans += pos - sum;
                sum = pos;
            }
            sum += x;
        }
        printf("Case #%d: %d\n", test + 1, ans);
    }
}
