#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int solve(int n, int x, vector<int> & a) {
    sort(a.begin(), a.end());

    int ans = 0;

    int p = a.size() - 1;
    for (int i = 0; i <= p; ++i) {
        while (p > i && a[p] + a[i] > x)
            --p, ++ans;
        ++ans;
        --p;
    }

    return ans;
}

int main() {
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int n, x;
        cin >> n >> x;
        vector<int> a(n);
        for (int i = 0; i < n; ++i)
            cin >> a[i];
        printf("Case #%d: %d\n", test, solve(n, x, a));
    }
}
