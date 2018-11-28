#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen ("in.txt", "r", stdin);
    freopen("op.txt", "w", stdout);
    int i, j, t, k;
    cin >> t;
    k = 1;

    while(t --) {
        string s;
        int n, c = 0;
        cin >> n >> s;
        j = 0;

        for(i = 0; i < s.size(); i ++) {
            if(s[i] == '0') {
                continue;
            }

            if(j < i) {
                c += i - j;
                j += i - j;
            }

            j += s[i] - '0';
        }
        cout << "Case #" << k << ": " << c << endl;
        k ++;
    }

    return 0;
}
