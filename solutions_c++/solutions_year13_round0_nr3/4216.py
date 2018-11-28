#include <cstdio>
#include <cmath>
#define infile "fairandsquare.in"
#define outfile "fairandsquare.out"
#define bMax 10000013
#define ll long long

using namespace std;

int cnt[bMax];
ll a, b, res;

bool isPalindrom(ll x) {
    ll y = 0, z = x;

    while(z) {
        y = y*10 + z%10;
        z /= 10;
    }

    return x == y;
}

void initialization() {
    for (int i = 1; i < bMax; ++i) {

        if (isPalindrom(i) && isPalindrom((ll)i * (ll)i)) {
            cnt[i] = 1;
        }

        cnt[i] += cnt[i-1];
    }
}

void read() {
    scanf("%lld %lld\n", &a, &b);
}

void solve() {
    ll le = sqrt(a);
    ll ri = sqrt(b);

    if (le*le < a) le++;

    res = cnt[ri] - cnt[le-1];
}

void write(int test) {
    printf("Case #%d: %lld\n", test, res);
}

int main() {
    freopen(infile, "r", stdin);
    freopen(outfile, "w", stdout);

    int n;
    scanf("%d\n", &n);

    initialization();

    for (int i = 0; i < n; ++i) {
        read();
        solve();
        write(i+1);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
