#include <bits/stdc++.h>
using namespace std;
const int MAXB = 1005;
typedef long long ll;
int B, k;
int ar[MAXB];
bool check(ll tm)
{
    ll sum = 0;
    int rm = 0;
    for (int i = 1; i <= B; ++i) {
        sum += (tm / ar[i])+1;
        if (sum >= k) {
            return true;
        }
    }
    if (sum)
    return false;
}
int get(ll tm)
{
    ll sum = 0;
    for (int i = 1; i <= B; ++i) {
        sum += (tm / ar[i]) + 1;
        if (0 == tm % ar[i]) {
            --sum;
        }
    }
    int rm = k-sum;
    for (int i = 1; i <= B; ++i) {
        if (0 == tm%ar[i]) {
            --rm;
            if (rm == 0) {
                return i;
            }
        }
    }
    return -1; // fucked
}
int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> B >> k;
        for (int i = 1; i <= B; ++i) {
            cin >> ar[i];
        }
        long long l = -1, r = ll( 1e10 * 1e5 );
        while (l+1 < r) {
            long long m = (l+r)/2;
            if (check(m)) {
                r = m;
            } else {
                l = m;
            }
        }
        printf("Case #%d: %d\n", t, get(r));
    }
    return 0;
}
