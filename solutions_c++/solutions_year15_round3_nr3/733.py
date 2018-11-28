#include <bits/stdc++.h>

#define maxN 1005
#define maxC 1000000007

using namespace std;

int a[maxN], c, d, v;
bool f[maxN];

int main() {
    #ifndef ONLINE_JUDGE
        freopen("C-small-attempt0.in", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif // ONLINE_JUDGE

    int nTest;
    scanf("%d", &nTest);

    for (int iTest = 1; iTest <= nTest; ++iTest) {
        scanf("%d%d%d", &c, &d, &v);
        for (int i = 0; i < d; ++i) scanf("%d", &a[i]);

        bool stop = false;
        int ans = 0;
        while (!stop) {
            for (int i = 0; i <= v; ++i) f[i] = false;
            f[0] = true;
            for (int i = 0; i < d; ++i) {
                for (int j = v; j >= a[i]; --j) {
                    if (f[j - a[i]]) f[j] =true;
                }
            }
        /*
            for (int i = 0; i <= v; ++i) printf("%d ", f[i]);
            printf("\n");
        */
            stop = true;
            for (int i = 1; i <= v; ++i) {
                if (!f[i]) {
                    a[d++] = i;
                    ++ans;
                    sort(a, a+d);
                    stop = false;
                    break;
                }
            }
        }

        printf("Case #%d: %d\n", iTest, ans);
    }

    return 0;
}
