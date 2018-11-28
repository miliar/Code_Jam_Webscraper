#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int a[int(2e3)];

int main() {
    int test;
    scanf("%d", &test);
    for ( int t = 1; t <= test; t++) {
        int n;
        scanf("%d", &n);
        for ( int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        long long ans = 2000;
        for ( int h = 1; h < 1001; h++) {
            long long col = h;
            for ( int i = 0; i < n; i++) {
                if (a[i] > h)
                    col += (a[i] - 1) / h;
            }
            ans = min(ans, col);
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
