#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int seen;
bool dig[10];

void see(int x) {
    while(x) {
        if (!dig[x%10]) {
            seen++;
            dig[x%10] = true;
        }
        x /= 10;
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T, n; scanf("%d", &T);
    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%d", &n);

        if (n==0) {
            printf("Case #%d: INSOMNIA\n", ncase);
            continue;
        }

        memset(dig, false, sizeof(dig));
        seen = 0;
        for(int ans=n; ; ans+=n) {
            see(ans);
            if (seen == 10) {
                printf("Case #%d: %d\n", ncase, ans);
                break;
            }
        }
    }

    return 0;
}
