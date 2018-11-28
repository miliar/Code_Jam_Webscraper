#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);

    for (int times = 0; times < T; times++) {
        int n;
        scanf("%d", &n);

        int val[1000];
        for (int i = 0; i < n; i++) {
            scanf("%d", &val[i]);
        }

        int myMin = 1000000000;
        for (int i = 1; i <= 1000; i++) {
            int t = 0;
            for (int j = 0; j < n; j++) {
                t += (val[j] - 1) / i;
            }
            myMin = min(myMin, t + i);
        }

        printf("Case #%d: %d\n", times + 1, myMin);
    }
}
