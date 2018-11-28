#include <cstdio>
#include <algorithm>
#define scanf(args...) (scanf(args) ? : 0)
const int MAXLEN = 1005;
const int INF = 1e9;

char str[MAXLEN];

int main() {
    int t;
    scanf("%d", &t);

    for (int test=1; test<=t; test++) {
        int n;
        scanf("%d%s", &n, str);

        int res = 0, count = 0;
        for (int i=0; i<n+1; i++) {
            if (i > count)
                res = std::max(res, i-count);
            count += str[i]-'0';
        }

        printf("Case #%d: %d\n", test, res);
    }
}
