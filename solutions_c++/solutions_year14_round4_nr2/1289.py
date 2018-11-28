#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int n;

int a[15];
int b[15];

int main() {
    int T;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin>>T;
    for (int cas = 1; cas <= T; cas++) {
        int ans = 2147483647;
        cin>>n;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            b[i] = i;
        }
        do {
            bool wa = 0;
            int p = -1;
            for (int i = 0; i < n - 1; i++)
                if (a[b[i]] > a[b[i + 1]]) {
                    p = i;
                    break;
                }
            if (p == -1) {
                int cnt = 0;
                for (int i = 0; i < n; i++)
                    for (int j = 0; j < i; j++)
                        if (b[j] > b[i]) cnt++;
                if (ans > cnt) {
                    ans = cnt;
                    //                    for (int i = 0; i < n; i++)
                    //                        printf("%d ", b[i]);
                    //                    printf("\n");
                }
                continue;
            }
            for (int i = p; i < n - 1; i++)
                if (a[b[i]] < a[b[i + 1]]) {
                    wa = 1;
                    break;
                }
            if (wa) continue;
            int cnt = 0;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < i; j++)
                    if (b[j] > b[i]) cnt++;
            if (ans > cnt) {
                ans = cnt;
                //                for (int i = 0; i < n; i++)
                //                    printf("%d ", b[i]);
                //                printf("\n");
            }
        } while (next_permutation(b, b + n));

        printf("Case #%d: %d\n", cas, ans);
    }

    return 0;
}