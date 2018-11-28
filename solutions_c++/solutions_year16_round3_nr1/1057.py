#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

ii v[32];

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T; scanf("%d", &T);

    for(int ncase=1; ncase<=T; ncase++) {
        int n, total=0;
        scanf("%d", &n);

        for(int i=0; i<n; i++) {
            scanf("%d", &v[i].first);
            v[i].second = i;
            total += v[i].first;
        }

        printf("Case #%d:", ncase);

        sort(v, v+n);
        while(v[n-1].first) {
            if (v[n-1].first == v[n-2].first && total != 3) {
                printf(" %c%c", v[n-1].second + 'A', v[n-2].second + 'A');
                v[n-1].first--;
                v[n-2].first--;
                total -= 2;
            }
            else {
                printf(" %c", v[n-1].second + 'A');
                v[n-1].first--;
                total--;
            }

            sort(v, v+n);
        }
        printf("\n");
    }

    return 0;
}
