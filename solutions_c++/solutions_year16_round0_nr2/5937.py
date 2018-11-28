#include <iostream>
using namespace std;

void solve () {
    string s;
    cin >> s;
    int len = s.size();
    int l, r;
    for (int i=len-1; i>=0; i--)
        if (s[i] == '-') {
            r = i;
            break;
        }
    int tot = 0;
    while (r >= 0) {
        l = 0;
        int incre = 0;
        while (s[l] == '+' && l < r) {
            s[l] = '-';
            l++;
            incre = 1;
        }
        if (incre == 1) tot++;
        char b[1000];
        for (int i=r; i>=0; i--)
            b[i] = s[i];
        for (int i=r; i>=0; i--)
            if (b[r-i] == '+')
                s[i] = '-';
            else
                s[i] = '+';
        tot++;
        //cout << tot << " " << s << endl;
        while (r >=0 && s[r] == '+') r--;
    }
    cout << tot << endl;
}

int main () {
    int t;
    cin >> t;
    for (int i=1; i<=t; i++) {
        cout << "Case #" << i << ": ";
        solve ();
    }
}