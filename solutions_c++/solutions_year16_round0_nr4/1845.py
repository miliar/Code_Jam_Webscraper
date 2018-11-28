#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
#include <fstream>
#define mp(a, b) make_pair(a, b)
using namespace std;

typedef unsigned long long int int64;

int64 calc(int64 i, int64 c, int64 k) {
    int64 left = i;
    while (c > 1) {
        left = (left - 1) * k + i;
        --c;
    }
    return left;
}

int main() {
    int64 t;
    cin >> t;
    for (int64 i = 1; i <= t; ++i) {
        int64 k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << i << ":";
        if (k == s) {
            for (int64 j = 1; j <= s; ++j) {
                cout << " " << calc(j, c, k);
            }
        } else {
            cout << " IMPOSSIBLE";
        }
        cout << "\n";
    }
    return 0;
}
