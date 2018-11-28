#include <bits/stdc++.h>

using namespace std;

int main() {
    int t; cin >> t;
    int tc = 1;
    while (t -- ) {
        int n; string s;
        cin >> n >> s;

        int standing = s[0] - '0' , res = 0;
        for (int i=1; i< s.size(); i++) {
            if (standing < i && s[i] - '0' > 0) {
                int d = i - standing;
                standing += d;
                res += d;
            }
            standing += s[i] - '0';
        }
        cout << "Case #"<< tc++ << ": " << res << endl;
    }
    return 0;
}
