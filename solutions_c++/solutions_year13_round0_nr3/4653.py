#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

struct Long {
    string s;
    void in () {
        cin >> s;
    }
    bool operator <= (const Long &x) {
        if (s.length() < x.s.length()) return 1;
        if (s.length() > x.s.length()) return 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] < x.s[i]) return 1;
            if (s[i] > x.s[i]) return 0;
        }
        return 1;
    }
    void operator = (string x) {
        s = x;
    }
}A, B;

Long a[20];

int main()
{
    a[0] = "1"; a[1] = "4"; a[2] = "9";
    a[3] = "121"; a[4] = "484";
    a[5] = "12321"; a[6] = "14641"; a[7] = "44944";
    a[8] = "1234321"; a[9] = "123454321"; a[10] = "125686521"; 
    a[11] = "12345654321"; a[12] = "1234567654321"; a[13] = "123456787654321"; a[14] = "12345678987654321";
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        int res = 0;
        A.in();
        B.in();
        for (int i = 0; i < 15; i++) {
            if (A <= a[i] && a[i] <= B) res++;
        }
        cout << "Case #" << tt << ": " << res << endl;
    }
    return 0;
}

