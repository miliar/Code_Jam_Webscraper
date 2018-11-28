#include <bits/stdc++.h>
using namespace std;

int pref[10001];

int mult(int a, int b) {
    if(a == 1) {
        return b;
    }
    if(a == 2) {
        if(b == 1) return a;
        if(b == -1) return -a;
        if(b == 2) return -1;
        if(b == -2) return 1;
        if(b == 3) return 4;
        if(b == -3) return -4;
        if(b == 4) return -3;
        if(b == -4) return 3;
    }
    if(a == 3) {
        if(b == 1) return a;
        if(b == -1) return -a;
        if(b == 2) return -4;
        if(b == -2) return 4;
        if(b == 3) return -1;
        if(b == -3) return 1;
        if(b == 4) return 2;
        if(b == -4) return -2;
    }
    if(a == 4) {
        if(b == 1) return a;
        if(b == -1) return -a;
        if(b == 2) return 3;
        if(b == -2) return -3;
        if(b == 3) return -2;
        if(b == -3) return 2;
        if(b == 4) return -1;
        if(b == -4) return 1;
    }
    if(a < 0) return -mult(-a, b);
}

int power(int a, int exp) {
    if(exp == 0) return 1;
    int t = power(a, exp/2);
    t = mult(t, t);
    if(exp % 2 != 0)
        t = mult(t, a);
    return t;
}

void solve() {
    long long l, x;
    cin >> l >> x;
    string l_str;
    cin >> l_str;

    int i_first = -1;
    int j_next = -1;
    pref[0] = 1;
    for(int i = 1; i <= l; ++i) {
        char ch = l_str[i - 1];
        int a = 1;
        if(ch == 'i') a = 2;
        else if(ch == 'j') a = 3;
        else a = 4;
        pref[i] = mult(pref[i - 1], a);
        if(pref[i] == 2 && i_first == -1) i_first = i;
        if(pref[i] == 4 && i_first > 0 && j_next < 0) j_next = i;
    }
    for(int i = 1; i <= 8 && i < x; ++i) {
        int cur = power(pref[l], i);
        for(int i = 1; i <= l; ++i) {
            char ch = l_str[i - 1];
            int a = 1;
            if(ch == 'i') a = 2;
            else if(ch == 'j') a = 3;
            else a = 4;
            cur = mult(cur, a);
            if(cur == 2 && i_first == -1) i_first = i;
            if(cur == 4 && i_first > 0 && j_next < 0) j_next = i;
        }
    }
    int total_prod = power(pref[l], x);
    string res = "NO";
    if(i_first > 0 && j_next > 0 && total_prod == -1)
        res = "YES";

    cout << res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cout.precision(30);

    int T;
    cin >> T;
    for(int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": ";
        solve();
        cout << endl;
    }

    return 0;
}
