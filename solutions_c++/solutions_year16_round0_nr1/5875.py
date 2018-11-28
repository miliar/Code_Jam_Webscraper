#include <iostream>
using namespace std;

void solve () {
    string s;
    int a[1000], b[1000], mark[10], cnt = 0, la;
    memset (a, 0, sizeof(a));
    memset (b, 0, sizeof (b));
    cin >> s;
    if (s == "0") {
        cout << "INSOMNIA\n";
        return;
    }
    for (int i=0; i<=9; i++)
        mark[i] = 0;
    
    int len = s.size();
    la = len;
    for (int i=0; i<len; i++) {
        b[i] = a[i] = s[len - i - 1] - '0';
        if (mark[a[i]] == 0) {
            mark[a[i]]++;
            cnt++;
        }
    }
    
    while (cnt < 10) {
        int add = 0;
        for (int i=0; i<la; i++) {
            b[i] += a[i] + add;
            add = b[i]/10;
            b[i] %= 10;
        }
        if (add) {
            b[la] = add;
            la++;
        }
        for (int i=0; i<la; i++) {
            if (mark[b[i]] == 0) {
                mark[b[i]]++;
                cnt++;
            }
        }
    }
    for (int i = la-1; i >= 0; i--)
        cout << b[i];
    cout << endl;
    
}

int main () {
    int t;
    cin >> t;
    for (int i=1; i<=t; i++) {
        cout << "Case #" << i << ": ";
        solve ();
    }
}