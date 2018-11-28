#include <stdio.h>
#include <vector>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int a[16];

int main() {
    int T;
    scanf("%d", &T);
    rep (_q, T) {
        rep (i, 16) a[i] = 1;
        rep (_, 2) {
            int x;
            scanf("%d", &x);
            x--;
            rep (i, 4) rep (j, 4) {
                int v;
                scanf("%d", &v);
                a[v-1] &= (x == i);
            }
        }
        vector<int> v;
        rep (i, 16) if (a[i]) v.push_back(i+1);
        printf("Case #%d: ", _q+1);
        if (v.size() == 1) printf("%d\n", v[0]);
        else if (v.size() > 0) printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");
    }
    return 0;
}
