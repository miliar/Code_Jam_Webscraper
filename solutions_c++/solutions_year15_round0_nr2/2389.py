#include <iostream>
#include <fstream>
using namespace std;
typedef long long ll;
typedef long double ld;

int T;
int n,a[1005];

int main()
{
    /// freopen("input.txt", "r", stdin);
    /// freopen("output.txt", "w", stdout);

    scanf("%d",&T);
    for (int TTT = 1; TTT <= T; ++TTT) {
        scanf("%d",&n);
        for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
        int ans = 2e9;
        for (int i = 1; i <= 1000; ++i) {
            int cur = 0;
            int maxstack = 0;
            for (int j = 0; j < n; ++j) {
                if (a[j] > i) {
                    maxstack = i;
                    cur += (a[j] - 1) / i;
                } else maxstack = max(maxstack, a[j]);
            }
            cur += maxstack;
            ans = min(ans, cur);
        }
        printf("Case #%d: %d\n", TTT, ans);
    }

    return 0;
}
