#include <bits/stdc++.h>
using namespace std;

const int N = 10;
const int mod = INT_MAX;

int number[N];

bool verify(int m) {

    int tmp = m;
    while (tmp > 0) {
        number[tmp%10] = 1;
        tmp /= 10;
    }

    bool flag = true;
    for (int i = 0; i < N; i++)
        flag = flag && number[i];

    return flag;
}

int main() {

    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    int t, n;
    scanf("%d", &t);

    for (int j = 1; j <= t; j++) {
        scanf("%d", &n);
        for (int i = 0; i < N; i++) number[i] = 0;
        int k = 1, m;
        while (k <= INT_MAX) {
            m = (n % mod * k % mod) % mod;
            if (verify(m) || n == 0) break;
            k++;
        }

        printf("Case #%d: ", j);
        if (n == 0)
            printf("INSOMNIA\n");
        else
            printf("%d\n", m);
    }

    return 0;
}
