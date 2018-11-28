#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;

int main() {
    freopen("D-small-attempt2.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        int k, c, s;
        cin >> k >> c >> s;
        ull a = 1;
        for (int i = 0; i < c; i++, a *= k);
        ull b = (k == 1 ? 1 : (a - 1) / (k - 1));
        cout << "Case #" << t << ": ";
        for (ull i = 1; i <= a; i += b)
            cout << i << " ";
        cout << endl;
    }
    return 0;
}
