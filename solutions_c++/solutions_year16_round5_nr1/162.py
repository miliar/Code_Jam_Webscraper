#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long ll;

char s[100005];

char st[100005];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        scanf("%s", s);
        int n = strlen(s);
        int m = 0;
        int ans = 0;
        for(int i = 0; i < n; ++ i) {
            if(m && st[m - 1] == s[i]) {
                -- m;
                ans += 10;
            } else {
                st[m ++] = s[i];
            }
        }
        ans += m / 2 * 5;
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
