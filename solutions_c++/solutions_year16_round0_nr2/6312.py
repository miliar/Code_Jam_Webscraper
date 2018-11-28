#include <bits/stdc++.h>

using namespace std;

string zip(string x) {
    string s = "";
    char prev = '\0';
    int i = 0;
    while (i < x.size()) {
        if (x[i] != prev) s += x[i];
        prev = x[i++];
    }
    return s;
}

int count(string x, char y) {
    int c = 0;
    for (int i = 0; i < x.size(); ++i) {
        if (x[i] == y) c++;
    }
    return c;
}

int main() {
    int t, q = 1;
    string x;
    cin >> t;
    while (t--) {
        cin >> x;
        x = zip(x);
        int ans;
        if (x[0] == '+') {
            ans = count(x, '-') * 2;
        } else {
            ans = (count(x, '-') * 2) - 1;
        }
        cout << "Case #" << q++ << ": " << ans << endl;
    }
    return 0;
}
