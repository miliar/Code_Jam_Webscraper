#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef unsigned long long llu;

const int MAX = 1e5 + 7;
int flag;

void checkDigit (ll num) {
    while (num) {
        int temp = num % 10;
        num /= 10;
        flag |= (1 << temp);
    }
}

int main () {
    freopen ("A-large.in", "r", stdin);
    freopen ("A-large.out", "w", stdout);
    int t;
    scanf ("%d", &t);

    for (int kase = 1; kase <= t; kase++) {
        ll n;
        scanf ("%lld", &n);

        printf ("Case #%d: ", kase);
        if (!n) printf ("INSOMNIA\n");
        else {
            flag = 0;
            ll incr = 0;
            while (flag != ((1 << 10) - 1)) {
                incr += n;
                checkDigit (incr);
            }
            printf ("%lld\n", incr);
        }
    }

    return 0;
}
