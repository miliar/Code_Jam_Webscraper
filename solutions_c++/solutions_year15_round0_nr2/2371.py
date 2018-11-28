#include <stdio.h>
#include <algorithm>
#include <functional>
using namespace std;

int testsCnt;
int n, a[1010];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &testsCnt);
    for (int testN = 1; testN <= testsCnt; testN++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        sort(a, a + n, greater<int>());
        int minR = 1010;
        for (int i = 1; i < 1010; i++) {
            int curR = 0;
            for (int j = 0; j < n; j++)
                if (a[j] > i)
                    curR += (a[j] - i) / i + ((a[j] - i) % i ? 1 : 0);
            minR = min(minR, curR + i);
        }
        printf("Case #%d: %d\n", testN, minR);
    }
}