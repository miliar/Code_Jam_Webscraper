#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <cstdio>

using namespace std;


int main() {
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int n;
        cin >> n;
        vector<int> a;
        a.resize(n);
        for (int i = 0; i < n; ++i)
            cin >> a[i];

        vector<int> b = a;

        sort(b.begin(), b.end());

        int l = 0, r = n - 1;
    
        int ans = 0;

        for (int i = 0; i < b.size(); ++i) {
            int pos = find(a.begin(), a.end(), b[i]) - a.begin();
            if (pos - l <= r - pos) {
                while (pos > l) {
                    swap(a[pos - 1], a[pos]);
                    ++ans;
                    --pos;
                }
                ++l;
            } else {
                while (pos < r) {
                    swap(a[pos], a[pos + 1]);
                    ++ans;
                    ++pos;
                }
                --r;
            }
        }

        printf("Case #%d: %d\n", test, ans);
    }
}
