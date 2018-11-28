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

int msk(ll a) {
    int result = 0;
    while (a != 0) {
        result |= 1 << (a % 10);
        a /= 10;
    }
    return result;
}

void solve() {
    long long n = next< int >();
    if (n == 0) {
        cout << "INSOMNIA\n";
        return;
    }
    int end = (1 << 10) - 1;
    int cur = msk(n);
    ll out = n;
    while (cur != end) {
        out += n;
        cur |= msk(out);
    }
    cout << out << endl;
}

int main() {
    int n = next< int >();
    for (int i = 1; i <= n; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
