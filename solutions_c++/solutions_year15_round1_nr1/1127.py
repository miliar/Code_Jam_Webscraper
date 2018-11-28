#include <bits/stdc++.h>

using namespace std;

#define N 1005

int arr[N];
int n;

int main() {
    int test;

    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);

    scanf("%d", &test);

    for (int cas = 1; cas <= test; cas++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", arr + i);
        }
        int ra = 0;
        for (int i = 0; i < n - 1; i++) {
            ra += max(0, arr[i] - arr[i + 1]);
        }
        int rb = 0;
        int ma = 0;
        int mm = 0;
        for (int i = 0; i < n - 1; i++) {
            int tm = max(0, arr[i] - arr[i + 1]);
            mm = max(tm, mm);
        }

        //cout << endl;

        //cout << ma << endl;

        for (int i = 0; i < n - 1; i++) {
            int tmp = arr[i] - arr[i + 1];

            rb += min(mm, arr[i]);

            //cout << rb - tt << endl;

        }

        printf("Case #%d: %d %d\n", cas, ra, rb);
    }
    return 0;
}
