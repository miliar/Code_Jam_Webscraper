/* Task solution for GCJ 2015
 * Tested with GCC
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

class /*Dumb*/Quaternion
{
    int val; // 1='1', 2='i', 3='j', 4='k', negative for '-'
public:
    Quaternion(char c = 'h') { // Hacky! (default 'h' is for '1')
        val = c - 'g';
    }
    Quaternion operator* (Quaternion q) const {
        static const int mul[4][4] = {
            {1,  2,  3,  4},
            {2, -1,  4, -3},
            {3, -4, -1,  2},
            {4,  3, -2, -1},
        };
        int sgn = val * q.val;
        sgn /= abs(sgn);
        Quaternion res;
        res.val = sgn * mul[abs(val) - 1][abs(q.val) - 1];
        return res;
    }
    Quaternion operator*= (Quaternion q) {
        return *this = *this * q;
    }
    Quaternion pow(int p) const {
        p %= 4;
        Quaternion res;
        while (p) {
            res *= *this;
            --p;
        }
        return res;
    }
    Quaternion operator- () {
        Quaternion res;
        res.val = -res.val;
        return res;
    }
    bool operator== (Quaternion q) {
        return val == q.val;
    }
    bool operator!= (Quaternion q) {
        return !(*this == q);
    }
};

const int max_l = 10000;
Quaternion s[max_l];

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    cin >> skipws;
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        bool good = true;
        int l, x;
        {
            long long X;
            cin >> l >> X;
            x = (X >= 8) ? (8 + X % 4) : X;
        }
        Quaternion t;
        for (int i = 0; i < l; ++i) {
            char c;
            cin >> c;
            s[i] = c;
            t *= s[i];
        }
        if (t.pow(x) != -Quaternion()) {
            good = false;
        }
        int L;
        if (good) {
            int e = l * x - 2;
            L = 1;
            Quaternion m(s[0]), w('i');
            while (m != w && L < e) {
                m *= s[L % l];
                ++L;
            }
            if (m != w) {
                good = false;
            }
        }
        int R;
        if (good) {
            R = l * x - 1;
            Quaternion m(s[l - 1]), w('k');
            int e = L + 1;
            while (m != w && R > e) {
                --R;
                m = s[R % l] * m;
            }
            if (m != w) {
                good = false;
            }
        }
        cout << "Case #" << T << ": " << (good ? "YES" : "NO") << endl;
    }
    return 0;
}
