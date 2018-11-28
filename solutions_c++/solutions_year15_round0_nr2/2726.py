#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <algorithm>

#define N 1100

using namespace std;

int n, p[N];


int main() {
    int cases;
    scanf("%d", &cases);
    for (int c = 1; c <= cases; c++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &p[i]);
        }
        int ans = 1001;
        for (int i = 1; i <= 1000; i++) {
            int k = 0;
            for (int j = 0; j < n; j++) {
                k += (p[j] - 1) / i;
            }
            k += i;
            if (k < ans) 
                ans = k;
        }
        printf("Case #%d: %d\n", c, ans);
    }
    return 0;
}


