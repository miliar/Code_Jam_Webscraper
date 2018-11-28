#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <functional>
#include <map>
#include <bitset>

#define INF 0x7fffffff
#define REP(i,j,k) for(int i = j;i <= k;i++)
#define squr(x) (x) * (x)
#define lowbit(x) (x&(-x))
#define getint(x) scanf("%d", &(x))

typedef long long LL;

using namespace std;

int n, m;
int T;
char s[1100];
bool f[1100];
int k;

int main(int argc, const char * argv[]) {
    freopen("A-large.in", "r", stdin);
    freopen("ans.out", "w", stdout);
    cin >> T;
    REP(ca, 1, T) {
        cin >> s;
        cin >> k;
        int len = strlen(s);
        int ans = 0;
        REP(i, 0, len - 1) {
            if (s[i] == '+') {
                f[i] = true;
            } else {
                f[i] = false;
            }
        }
        for (int i = 0; i < len - k + 1; i++) {
            if (!f[i]) {
                ans++;
                for (int j = i; j < i + k; j++) {
                    f[j] = !f[j];
                }
            }
        }
        for (int i = len - k; i < len; i++) {
            if (!f[i]) {
                ans = -1;
                break;
            }
        }
        if (ans == -1) {
            printf("Case #%d: IMPOSSIBLE\n", ca);
        } else {
            printf("Case #%d: %d\n", ca, ans);
        }
    }
    return 0;
}









