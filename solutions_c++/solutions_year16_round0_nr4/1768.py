#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);

    int T, K, C, S;
    scanf("%d", &T);
    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%d%d%d", &K, &C, &S);
        printf("Case #%d:", ncase);
        for(int i=1; i<=S; i++) printf(" %d", i);
        printf("\n");
    }

    return 0;
}
