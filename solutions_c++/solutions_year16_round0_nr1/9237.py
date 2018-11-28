#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

void mark(ll x, bool* dig) {
    while (x) {
        dig[x % 10] = true;
        x /= 10;
    }
}

bool allTrue(bool* dig) {
    for (int i = 0; i < 10; ++i)
        if (!dig[i])
            return false;
    return true;
}

ll solve(int n) {
    ll x = n;
    bool dig[10] = {0};
    mark(x, dig);
    while (!allTrue(dig)) {
        x += n;
        mark(x, dig);
    }
    return x;

}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int it = 1; it <= t; ++it) {
        int n;
        cin >> n;
        if (n != 0)
            printf("Case #%d: %lld\n", it, solve(n));
        else
            printf("Case #%d: INSOMNIA\n", it);
    }
    return 0;
}