#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <utility>

using namespace std;

typedef long long ll;

template<typename T>
T next() { T tmp; cin >> tmp; return tmp; }

void print(ll a, int size) {
    string result;
    for (int i = size - 1; i >= 0; --i) {
        result += (char)((a >> i) % 2 + '0');
    }
    cout << result;
}

void solve() {
    int n = next< int >();
    int j = next< int >();
    int base = n / 2;
    cout << endl;
    for (ll ii = 0; ii < j; ++ii) {
        ll i = ii + (1 << (base - 2));
        ll a = (i * 2 + 1);
        ll num = (a << base) + a;
        print(num, n);
        for (int b = 2; b <= 10; ++b) {
            ll divisor = 0;
            ll mult = 1;
            for (int j = 0; j < base; ++j) {
                divisor += (a >> j) % 2 * mult;
                mult *= b;
            }
            cout << " " << divisor;
        }
        cout << endl;
    }
}

int main() {
    int n = next< int >();
    for (int i = 1; i <= n; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
