#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <sstream>
using namespace std;

int tests, n, m, l;
string a[2000], b;

int main() {
    cin >> tests;
    for (int cases = 1; cases <= tests; ++ cases) {
        cin >> n >> l;
        for (int i = 0; i < n; ++ i) cin >> a[i];
        cin >> b;
        bool mark = true;
        for (int i = 0; i < n; ++ i)
            if (a[i] == b) {
                mark = false;
                break;
            }
        if (!mark) {
            cout << "Case #" << cases << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << cases << ": ";
            for (int i = 0; i < l; ++ i)
                cout << (1 - (b[i] - '0')) << '?';
            cout << ' ';
            for (int i = 0; i < l - 1; ++ i)
                cout << (1 - (b[i] - '0')) << int (b[i] - '0');
            cout << (1 - (b[l - 1] - '0')) << endl;
        }
    }
    return 0;
}

