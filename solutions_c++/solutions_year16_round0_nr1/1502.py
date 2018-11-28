#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int m = 10000005;

int n;
bool mark[10];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int nTests = 0;
    scanf("%d", &nTests);
    for(int Case = 1; Case <= nTests; ++Case) {
        scanf("%d", &n);
        ll tmp = 0;
        memset(mark, false, sizeof mark);
        int cnt = 0;
        for(int i = 1; i < m; ++i) {
            tmp += n;
            ll s = tmp;
            do {
                int b = tmp % 10;
                cnt += (mark[b] == false);
                mark[b] = true;
                tmp /= 10;
            } while (tmp > 0);
            tmp = s;
            if (cnt == 10) break;
        }
        printf("Case #%d: ", Case);
        if (cnt == 10) printf("%I64d\n", tmp);
        else printf("INSOMNIA\n");
    }
    return 0;
}

