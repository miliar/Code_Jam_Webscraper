#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    int i = 0;
    while (test--) {
        ++i;
        int mx;
        string s;
        cin >> mx >> s;
        int ans = 0;
        vector <int> v;
        v.clear();
        for (int j = 1; j < s.length(); ++j)
            for (int k = 1; k <= s[j] - '0'; ++k)
                v.push_back(j);
        int cur = s[0] - '0';
        for (int j = 0; j < v.size(); ++j) {
            if (cur < v[j]) {
                ans+=v[j] - cur;
                cur+=v[j] - cur;
            }
            ++cur;
        }
        cout << "Case #" << i << ": " << ans << endl;
    }

    return 0;
}
