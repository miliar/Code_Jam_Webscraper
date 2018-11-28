#include <bits/stdc++.h>

using namespace  std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("2.txt", "w", stdout);

    int t;
    cin >> t;

    for (int cs = 0; cs < t; cs++) {
        string a, s = "";
        cin >> a;
        for (int i = 0; i < a.size(); i++) {
            s += a[i];
            for (int j = i + 1; j < a.size() && (a[i] == a[j]); j++) {
                i = j;
            }
        }
        cout << "Case #" << cs + 1 << ": " << (int)s.size() - (int)(s[s.size()-1] == '+') << endl;
    }

    return 0;
}


