#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define ll long long
#define INF 1000000007

using namespace std;

char s[200];

void solve() {
    int n = strlen(s + 1);
    while (n && s[n] == '+') -- n;
    int ans = 0;
    for (int i = 2; i <= n; ++ i)
        if (s[i - 1] != s[i]) ++ ans;
    if (n) ++ ans;
    printf("%d\n", ans);
}

int main() {
    
   // freopen("test.in", "r", stdin);
   // freopen("test.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++ t) {
        scanf("%s", s + 1);
        printf("Case #%d: ", t);
        solve();
    }
    return 0;

}

