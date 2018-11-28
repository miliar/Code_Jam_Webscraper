#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);

    int t;
    cin >> t;
    for(int tt = 1; tt <= t; ++tt) {
        string str;
        cin >> str;
        str += "+";

        int ops = 0;
        for(int i = 1; i < str.length(); ++i) {
            if(str[i] != str[i - 1]) {
                ops += 1;
            }
        }

//        cerr << x << '\n';
        cout << "Case #" << tt << ": " << ops << '\n';
    }

    return 0;
}
