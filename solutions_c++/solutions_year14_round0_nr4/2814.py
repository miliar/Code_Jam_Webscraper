#include <cstdio>
#include <algorithm>
using namespace std;
double me[1000];
double he[1000];
bool taken[1000];
int n;
int normal() {
    int ans = 0;
    for (int i = 0; i < n; i++) {
        taken[i] = false;
    }
    for (int i = 0; i < n; i++) {
        int idx = -1;
        int fst = 1000000;
        for (int j = 0; j < n; j++) {
            if (!taken[j]) {
                fst = min(fst, j);
                if (he[j] > me[i]) {
                    idx = j;
                    break;
                }
            }
        }
        taken[idx] = true;
        if (me[i] > he[idx]) {
            ans++;
        }
    }
    return ans;
}

int fake() {
    int ans = 0;
    int meIdx = 0;
    int heIdx = 0;
    while (heIdx < n && meIdx < n) {
        while (meIdx < n && me[meIdx] < he[heIdx]) {
            meIdx++;
        }
        if (meIdx < n) {
            ans++;
            meIdx++;
            heIdx++;
        }
    }
    return ans;
}

int main() {
    int tests;
    scanf("%d", &tests);
    for (int t = 1; t <= tests; t++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%lf", &me[i]);
        }
        for (int i = 0; i < n; i++) {
            scanf("%lf", &he[i]);
        }
        sort(me, me + n);
        sort(he, he + n);

        printf("Case #%d: %d %d\n", t, fake(), normal());
    }
    return 0;
}
