#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAX_N = 1001;
int T, n;
double N[MAX_N], K[MAX_N];

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("d.out", "w", stdout);
    cin >> T;
    for (int cs = 1; cs <= T; ++cs) {
        cin >> n;
        for (int i = 0; i < n; ++i)
            cin >> N[i];
        for (int i = 0; i < n; ++i)
            cin >> K[i];
        sort(N, N + n);
        sort(K, K + n);
        
        int ans1 = 0, ans2 = n;
        for (int i = 0, l = 0, r = n - 1; i < n; ++i) {
            if (N[i] > K[l]) ++l, ++ans1;
            else --r;
        }
        for (int i = 0, j = 0; i < n; ++i, ++j) {
            while (j < n && K[j] < N[i]) ++j;
            if (j < n) --ans2;
            else break;
        }
        printf("Case #%d: %d %d\n", cs, ans1, ans2);
    }    
    return 0;
}
