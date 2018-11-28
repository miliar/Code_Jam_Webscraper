#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    cin >> t;

    int k = 0;
    while (k < t) {
        k++;
        cout << "Case #" << k << ": ";

        string s;
        int n;
        cin >> n;
        cin >> s;

        int d = 0;
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            int x = s[i] - '0';
            if (x > 0) {
                int j = max(i - d, 0);
                res += j;
                d += j;
            }
            d += x;
        }
        cout << res << endl;
    }

    return 0;
}
