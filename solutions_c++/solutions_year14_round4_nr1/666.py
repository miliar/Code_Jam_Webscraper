#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#define puba push_back

using namespace std;

int t, x, s, n;

int main() {
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cin >> n >> x;
        vector <int> mas;
        for (int j = 0; j < n; ++j) {
            cin >> s;
            mas.puba(s);
        }
        sort(mas.begin(), mas.end());
        int l = 0, r = n - 1;
        int ans = 0;
        while (r >= l) {
            if (mas[r] + mas[l] <= x && r != l) {
                ++ans;
                --r;
                ++l;
            } else {
                ++ans;
                --r;
            }
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    
    return 0;
}