#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>

using namespace std;
#define ll long long
#define pii pair<int, int>
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define VI vector<int>
#define all(s) (s).begin(),(s).end()
#define L(s) (int)(s).size()
#define inf 1000000000

int n, j;

int main() {
    n = 16;
    j = 50;
    freopen("output.txt", "w", stdout);
    cout << "Case #1:\n";
    for(int mask = 0; mask < (1 << (n - 2)); ++mask) {
        int val = (1 << (n - 1)) | (mask << 1) | 1;
        bool ok = 1;
        VI ret(0);
        for(int base = 2; base <= 10; ++base) {
            ll x = 0;
            for(int i = n - 1; i >= 0; --i) {
                x = x * base;
                if (val & (1 << i)) x++;
            }
            bool fnd = 0;
            for(int i = 2; 1LL * i * i <= x; ++i) {
                if (x % i == 0) {
                    fnd = 1;
                    ret.pb(i);
                    break;
                }
            }
            if (!fnd) {
                ok = 0;
                break;
            }
        }
        if (ok) {
            for(int i = n - 1; i >= 0; --i) {
                if (val & (1 << i)) cout << "1"; else cout << "0";
            }
            for(int i = 0; i < L(ret); ++i) {
                cout << " " << ret[i];
            }
            cout << endl;
            --j;
            cerr << "Remaining " << j << endl;
            if (!j) break;
        }
    }
}
