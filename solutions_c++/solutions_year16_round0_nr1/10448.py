#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

const int UP = 1000000;
using ll = long long;
int cn = 0;
bool cnt[10];
inline void cl(int x) {
    while (x) {
        int r = x % 10;
        if (!cnt[r]) {
            cnt[r] = 1;
            cn++;
        }
        x /= 10;
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    ll n;
    cin >> t;
    for (int k = 1; k <= t; k++) {
        cout << "Case #" << k << ": ";
        cn = 0;
        bool f = 0;
        cin >> n;
        memset(cnt, 0, sizeof(cnt));
        for (int i = 1; i < UP; i++) {
            ll q = n * i;
            cl(q);
            if (cn == 10) {
                cout << q << '\n';
                f = 1;
                break;
            }
        }
        if (!f) {
            cout << "INSOMNIA\n";
        }
    }
    return 0;
}
