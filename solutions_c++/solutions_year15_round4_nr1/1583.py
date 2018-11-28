#define DBG 1

#include <cstring>
#include <map>
#include <unordered_map>
#include <string>
#include <list>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <cstdio>
#include <iostream>
#include <set>
#include <unordered_set>
using namespace std;

#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int, int> pii;

int gi() {
    int a;
    scanf("%d", &a);
    return a;
}

ll gli() {
    ll a;
    scanf("%lld", &a);
    return a;
}

char l[104];
char r[104];
char a[104][104];

#define SINGLELINE 1
void solve() {
    int n = gi();
    int m = gi();
    int res = 0;
    memset(l, 0, sizeof(char) * n);
    memset(r, 0, sizeof(char) * m);
    for (int i = 0; i < n; i++) {
        scanf("%s", a[i]);
        for (int j = 0; j < m; j++) {
            char c = a[i][j];
            if (c != '.') {
                if (l[i] == 0 && c == '<')
                    res++;
                else if (r[j] == 0 && c == '^')
                    res++;
                l[i]++;
                r[j]++;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] != '.' && l[i] == 1 && r[j] == 1) {
                printf("IMPOSSIBLE\n");
                return;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            char c = a[i][j];
            if (c != '.') {
                l[i]--;
                r[j]--;
                if (l[i] == 0 && c == '>')
                    res++;
                else if (r[j] == 0 && c == 'v')
                    res++;
            }
        }
    }
    printf("%d\n", res);
}

int main() {
    int t = gi();

    for (int i = 1; i <= t; i++) {
        printf("Case #%d:%c", i, (SINGLELINE ? ' ' : '\n'));
        solve();
        fprintf (stderr, "Case %d / %d. Elapsed %.2f. Estimated %.2f\n", i, t, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / i * t) / CLOCKS_PER_SEC);
    }

    return 0;
}
