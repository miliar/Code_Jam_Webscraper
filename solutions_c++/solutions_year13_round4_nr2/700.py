#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <map>
#include <set>

using namespace std;

int main() {
    int tests;
    cin >> tests;
    for (int test_id = 1; test_id <= tests; ++test_id) {
        long long n, p;
        cin >> n >> p;
        --p;
        long long r1 = 0;
        long long cnt = 0;
        int i = n - 1;
        while (i >= 0 && (p & (1LL << i))) { ++cnt; --i; }
        cout << "Case #" << test_id << ": ";
        cout << min((1LL << n) - 1LL, (1LL << (cnt + 1)) - 2LL);
        cout << " ";
        long long tmp = 1LL;
        i = n - 1;
        while (i >= 0 && !(p & (1LL << i))) { --i; tmp *= 2LL; }
        bool ok = true;
        while (i >= 0) {
            if (!(p & (1LL << i))) ok = false;
            --i;
        }
        if (ok) cout << (1LL << n) - tmp << endl;
        else cout << (1LL << n) - 2LL * tmp << endl;
    }
    return 0;
}
