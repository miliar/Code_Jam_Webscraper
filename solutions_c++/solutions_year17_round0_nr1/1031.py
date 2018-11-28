#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int main() {
//    freopen("A-small-attempt0.in", "r", stdin);
//    freopen("A-small-attempt0.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    string str;
    int K;

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        cin >> str;
        scanf("%d", &K);
        int n = (int)str.size();
        int res = 0;
        for (int i = 0; i <= n - K; i++) {
            if (str[i] == '-') {
                for (int j = i; j < i + K; j++) {
                    str[j] = (str[j] == '+') ? '-' : '+';
                }
                res++;
            }
        }
        for (int i = n - K + 1; i < n; i++) {
            if (str[i] == '-') {
                res = -1;
                break;
            }
        }
        if (res == -1) {
            printf("Case #%d: IMPOSSIBLE\n", t);
        }
        else {
            printf("Case #%d: %d\n", t, res);
        }
    }

    return 0;
}

