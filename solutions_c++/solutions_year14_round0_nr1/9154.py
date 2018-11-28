#include <cstdio>
#include <set>
using namespace std;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        set<int> st;
        int cnt = 0, r, ans;
        scanf("%d", &r);
        for (int i = 0; i < 4; ++i) for (int  j = 0; j < 4; ++j) {
            if (i+1 == r) {
                int t;
                scanf("%d", &t);
                st.insert(t);
            }
            else scanf("%*d");
        }
        scanf("%d", &r);
        for (int i = 0; i < 4; ++i) for (int  j = 0; j < 4; ++j) {
            if (i+1 == r) {
                int t;
                scanf("%d", &t);
                if (st.find(t) != st.end()) {
                    ans = t;
                    ++cnt;
                }
            }
            else scanf("%*d");
        }
        printf("Case #%d: ", cas);
        if (cnt == 1) printf("%d\n", ans);
        else if (cnt == 0) puts("Volunteer cheated!");
        else puts("Bad magician!");
    }
    return 0;
}
