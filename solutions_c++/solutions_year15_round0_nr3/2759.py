#include <iostream>
#include <string>
using namespace std;

int ONE = 1, I = 2, J = 3, K = 4;
int table[5][5] = {{0, 0, 0, 0, 0}, \
                   {0, ONE, I, J, K}, \
                   {0, I, -ONE, K, -J}, \
                   {0, J, -K, -ONE, I}, \
                   {0, K, J, -I, -ONE}};

int get_num(char c) {
    if (c == '1') return 1;
    if (c == 'i') return 2;
    if (c == 'j') return 3;
    if (c == 'k') return 4;
    return 0;
}

void get_abs(int &x, int &ret) {
    if (x < 0) {
        ret *= -1;
        x *= -1;
    }
}

int mul(int x, int y) {
    int ret = 1;
    get_abs(x, ret);
    get_abs(y, ret);
    ret *= table[x][y];
    return ret;
}

int invmul(int inv, int y) {
    int ret = 1;
    for (int i = 1; i < 5; ++i) {
        get_abs(inv, ret);
        get_abs(y, ret);
        if (table[inv][i] == y) ret *= i;
        if (table[inv][i] == -y) ret *= (-i);
    }
    return ret;
}

int mulinv(int x, int inv) {
    int ret = 1;
    for (int i = 1; i < 5; ++i) {
        get_abs(inv, ret);
        get_abs(x, ret);
        if (table[i][inv] == x) ret *= i;
        if (table[i][inv] == -x) ret *= (-i);
    }
    return ret;
}


int main() {
    int t, L, X;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        string s;
        cin >> L >> X >> s;
        int lo = 0, hi = L*X-1;
        int xi = get_num(s[lo%L]), xk = get_num(s[hi%L]), xj = 1;
        while ((xi != I) && (lo < L*X - 1)) {
            ++lo;
            xi = mul(xi, get_num(s[lo%L]));
        }
        while ((xk != K) && (hi > 0)) {
            --hi;
            xk = mul(get_num(s[hi%L]), xk);
        }
        for (int j = lo+1; j < hi; ++j) xj = mul(xj, get_num(s[j%L]));
        cout << "Case #" << i << ": ";
        if ((lo < hi) && (xi == I) && (xj == J) && (xk == K)) cout << "YES";
        else cout << "NO";
        cout << endl;
    }
}