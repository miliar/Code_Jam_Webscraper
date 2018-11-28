#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int solve(string &s, int k) {
    int ans = 0, st = s[0] - '0';

    for (int i=1; i<=k; i++) {
        if (st < i) {
            ans += i - st;
            st = i;
        }
        st += s[i] - '0';
    }
    return ans;
}

int main() {
    int t, k;
    string s;
    cin >> t;
    for (int i=1; i<=t; i++) {
        cin >> k >> s;
        cout << "Case #" << i << ": " << solve(s, k) << endl;
    }
    return 0;
}
