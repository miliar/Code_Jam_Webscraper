#include <bits/stdc++.h>

using namespace std;
// const int MaxN = ;
// const int MOD = ;

int mp[10], tot = 10;
bool alldone = false;

void mark(int n, int i) {
        int mul = n * i;
        while (mul) {
                if (mp[mul % 10] == 0) {
                        mp[mul % 10] = 1;
                        --tot;
                }
                mul /= 10;
        }
        if (tot == 0) {
                alldone = true;
        }
}

int main() {
        freopen("A-large.in", "rt", stdin);
        freopen("A-large.out", "wt", stdout);
        int t;
        scanf("%d", &t);
        for (int tc = 0; tc < t; ++tc) {
                memset(mp, 0, sizeof(mp));
                tot = 10;
                alldone = false;
                printf("Case #%d: ", tc + 1);
                int n;
                scanf("%d", &n);
                int i;
                for (i = 1; i <= 72; ++i) {
                        mark(n, i);
                        if (alldone) {
                                break;
                        }
                }
                if (alldone) {
                        printf("%d\n", n * i);
                } else {
                        printf("INSOMNIA\n");
                }
        }
        return 0;
}
