#include<bits/stdc++.h>

using namespace std;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, tc = 1;
    cin >> T;
    while (T--) {
        int n;
        string s;
        cin >> n >> s;
        int ans = 0;
        vector<int> a;
        for (int i = 0; i < s.size(); i++) {
            for (int j = 0; j < s[i] - '0'; j++) {
                a.push_back(i);
            }
        }
        sort(a.begin(), a.end());
        int have = 0;
        for (int i = 0; i < a.size(); i++) {
            if (a[i] > have) {
                ans += a[i] - have;
                have = a[i];
            }
            have++;
        }
        cout << "Case #" << tc++ << ": " << ans << endl;
    }
    return 0;
}
