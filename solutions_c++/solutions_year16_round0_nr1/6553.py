#include<bits/stdc++.h>

#define int long long int

using namespace std;

int t, n;

int A[19];

int32_t main() {
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);

    scanf("%lld", &t);

    for (int h=1; h<=t; h++) {
        scanf("%lld", &n);

        bool zero = 0;

        memset(A, 0, sizeof(A));

        for (int i=1; i<=10000; i++) {
            int x = n*i;
            bool one = 0;

            while (x) {A[x%10] = 1; x /= 10;}

            for (int j=0; j<10; j++) if (A[j] == 0) {one = 1; break;}

            if (one == 0) {
                printf("Case #%lld: %lld\n", h, n*i);
                zero = 1; break;
            }
        }

        if (zero == 0) printf("Case #%lld: INSOMNIA\n", h);
    }

    return 0;
}
