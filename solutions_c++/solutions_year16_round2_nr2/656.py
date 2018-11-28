/* Task solution for GCJ 2015
 * Tested with GCC
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long long ll;

ll va, vb;

void upd(ll a, ll b) {
    //cout << "upd " << a << ' ' << b << endl;
    if (abs(va - vb) < abs(a - b)) {
        return;
    }
    if (abs(va - vb) == abs(a - b)) {
        if (va < a) {
            return;
        }
        if (va == a) {
            if (vb < b) {
                return;
            }
            if (vb == b) {
                cerr << "EQ!!!\n";
                return;
            }
        }
    }
    va = a;
    vb = b;
}

void chk(string a, string b) {
    //cout << "chk " << a << ' ' << b << endl;
    upd(stoll(a), stoll(b));
}

void sfx(string a, string b) {
    //cout << "sfx " << a << ' ' << b << endl;
    size_t i = 0;
    while (i < a.size() && a[i] == b[i]) {
        ++i;
    }
    if (i < a.size()) {
        char ca, cb;
        if (a[i] < b[i]) {
            ca = '9';
            cb = '0';
        } else {
            ca = '0';
            cb = '9';
        }
        ++i;
        while (i < a.size()) {
            if (a[i] == '?') {
                a[i] = ca;
            }
            if (b[i] == '?') {
                b[i] = cb;
            }
            ++i;
        }
    }
    chk(a, b);
}

void difpfx(string a, string b) {
    //cout << "difpfx " << a << ' ' << b << endl;
    size_t i = 0;
    while (i < a.size() && a[i] == b[i] && a[i] != '?') {
        ++i;
    }
    if (i >= a.size()) {
        sfx(a, b);
        return;
    }
    if (a[i] == '?') {
        if (b[i] == '?') {
            a[i] = '0';
            b[i] = '1';
            sfx(a, b);
            a[i] = '1';
            b[i] = '0';
            sfx(a, b);
        } else {
            if (b[i] != '0') {
                a[i] = b[i] - 1;
                sfx(a, b);
            }
            if (b[i] != '9') {
                a[i] = b[i] + 1;
                sfx(a, b);
            }
        }
    } else {
        if (b[i] == '?') {
            if (a[i] != '0') {
                b[i] = a[i] - 1;
                sfx(a, b);
            }
            if (a[i] != '9') {
                b[i] = a[i] + 1;
                sfx(a, b);
            }
        } else {
            sfx(a, b);
        }
    }
}

void eqpfx(string a, string b) {
    //cout << "eqpfx " << a << ' ' << b << endl;
    size_t i = 0;
    difpfx(a, b);
    for (;;) {
        while (i < a.size() && a[i] == b[i] && a[i] != '?') {
            ++i;
        }
        if (i >= a.size() || (a[i] != '?' && b[i] != '?')) {
            return;
        }
        if (a[i] == '?') {
            if (b[i] == '?') {
                b[i] = '0';
            }
            a[i] = b[i];
        } else {
            b[i] = a[i];
        }
        difpfx(a, b);
        ++i;
    }
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    cout << setfill('0');
    for (int T = 1; T <= TN; T++) {
        string a, b;
        cin >> a >> b;
        va = 2e18;
        vb = 0;
        eqpfx(a, b);
        cout << "Case #" << T << ": " << setw(a.size()) << va << ' ' << setw(a.size()) << vb << endl;
    }
    return 0;
}
