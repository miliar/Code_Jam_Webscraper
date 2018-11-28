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

char s[205];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        scanf("%s", s);
        int n = strlen(s);
        int ans = 0;
        for(int i = 1; i < n; ++ i) {
            ans += s[i] != s[i - 1];
        }
        if(s[n - 1] == '-') ++ ans;
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
