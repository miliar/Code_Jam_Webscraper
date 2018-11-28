#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair

#define eps 0.0000001
#define pi  3.14159265359
#define inf 2000000000

typedef long long lld;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

const int MAXN = 1000 + 5;

int n, k;
char s[MAXN];

char turn(char c) {
    return (c == '-') ? '+' : '-';
}

int main() {
    int tt;
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
        scanf("%s %d", s, &k);
        n = strlen(s);
        int sol = 0;
        for (int i = 0; i + k - 1 < n; i++) {
            if (s[i] == '-') {
                sol++;
                for (int j = i; j < i + k; j++) {
                    s[j] = turn(s[j]);
                }
            }
        }
        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                sol = -1;
                break;
            }
        }
        if (sol == -1) {
            printf("Case #%d: IMPOSSIBLE\n", t);
        } else {
            printf("Case #%d: %d\n", t, sol);
        }
    }
    return 0;
}
