#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int n, x;
        cin >> n >> x;
        vector<int> s(n);
        for (int i = 0; i < n; ++i) {
            cin >> s[i];
        }
        sort(s.begin(), s.end());
        int result = 0;
        for (int l = 0, r = n; l < r;) {
            if (s[l] + s[r - 1] <= x) {
                ++result;
                ++l;
                --r;
            } else {
                --r;
                ++result;
            }
        }
        cout << "Case #" << test << ": " << result << endl;
    }
}