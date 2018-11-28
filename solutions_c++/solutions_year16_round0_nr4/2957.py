#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        long long k, c, s;
        cin >> k >> c >> s;
        if (k == s) {
            cout << "Case #" << i << ":";
            long long f = 1;
            for (int j = 1; j < c; ++j) {
                f *= k;
            }
            for (long long j = 0; j < k; ++j) {
                cout << " " << j * f + 1;
            }
            cout << "\n";
        }
    }

    return 0;
}