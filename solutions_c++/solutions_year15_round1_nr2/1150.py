#include <bits/stdc++.h>

using namespace std;

const int INF = 1e9;
#define N 1005
#define LL long long

int arr[N];
int n, m;

LL calc(LL num) {
    if (num == -1) return 0;
    LL res = 0;
    for (int i = 0; i < n; i++) {
        res += num / arr[i] + 1;
    }
    return res;
}

int main() {
    int test;

    freopen("B-large.in", "r", stdin);
    freopen("b.out", "w", stdout);

    scanf("%d", &test);

    for (int cas = 1; cas <= test; cas++) {
        scanf("%d%d", &n, &m);
        int ma = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", arr + i);
            ma = max(ma, arr[i]);
        }
        LL R = (LL)ma * m;
        LL L = 0;
       // cout << calc(10) << endl;

        while (L <= R) {
            LL mid = L + R >> 1;
            if (calc(mid) >= m)
                R = mid - 1;
            else
                L = mid + 1;
        }
        int res = -1;

        int cnt = 0;

        int tar = m - calc(L - 1);

        for (int i = 0; i < n; i++) {
            if (L % arr[i] == 0) {
                cnt++;
                if (cnt == tar) {
                    res = i;
                    break;
                }
            }
        }

        printf("Case #%d: %d\n", cas, res + 1);
    }
    return 0;
}
