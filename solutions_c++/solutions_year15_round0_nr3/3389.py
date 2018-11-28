#include <iostream>
#include <stdio.h>
#include <assert.h>
#include <vector>

#pragma clang diagnostic push
#pragma ide diagnostic ignored "missing_default_case"
using namespace std;

struct quaternion {
    char c;
    int sign;

    quaternion(const quaternion &a) {
        this->c = a.c, this->sign = a.sign;
    }

    quaternion(char c, int sign) : c(c), sign(sign) { }

    quaternion() {

    }

    operator string() const {
        return (sign == -1 ? "-" : "") + c;
    }
};

quaternion operator*(const quaternion &a, const quaternion &b) {
    int newSign = a.sign * b.sign;
    if (a.c == '1') return quaternion(b.c, newSign);
    if (b.c == '1') return quaternion(a.c, newSign);
    if (a.c == b.c) return quaternion('1', -newSign);
    if (a.c == 'i') {
        if (b.c == 'j')
            return quaternion('k', newSign);
        if (b.c == 'k')
            return quaternion('j', -newSign);
    }
    if (a.c == 'j') {
        if (b.c == 'i')
            return quaternion('k', -newSign);
        if (b.c == 'k')
            return quaternion('i', newSign);
    }
    if (a.c == 'k') {
        if (b.c == 'i')
            return quaternion('j', newSign);
        if (b.c == 'j')
            return quaternion('i', -newSign);
    }
    assert(false);
}

bool operator==(const quaternion &a, const quaternion &b) {
    return a.c == b.c && a.sign == b.sign;
}

bool operator!=(const quaternion &a, const quaternion &b) {
    return !(a == b);
}

quaternion &operator*=(quaternion &a, const quaternion &b) {
    a = a * b;
    return a;
}

quaternion binpow(const quaternion &a, int n) {
    quaternion b = a;
    quaternion res('1', 1);
    while (n) {
        if (n & 1)
            res *= b;
        b *= b;
        n >>= 1;
    }
    return res;
}


string repeat(string a, int n) {
    string ans = "";
    for (int i = 0; i < n; ++i)
        ans += a;
    return ans;
}

bool test(int pow, string a) {
    a = repeat(a, pow);
    size_t n = a.size();
    if (n < 3) return false;
    vector<quaternion> suf(n);
    suf[n - 1] = quaternion(a[n - 1], 1);
    for (int i = n - 2; i >= 0; --i) {
        suf[i] = quaternion(a[i],1) * suf[i+1];
    }
    quaternion left('1', 1);
    for (size_t i = 0; i < n - 2; ++i) {
        left *= quaternion(a[i], 1);
        if (left == quaternion('i', 1)) {
            quaternion center('1', 1);
            for (size_t j = i + 1; j < n - 1; ++j) {
                center *= quaternion(a[j], 1);
                if (center == quaternion('j', 1)) {
                    if (suf[j + 1] == quaternion('k', 1))
                        return true;
                }
            }
        }

    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cerr << i << '\n';
        int n, l;
        string s;
        cin >> n >> l >> s;
        cout << "Case #" << i + 1 << ": " << (test(l, s) ? "YES" : "NO") << endl;
    }
}

#pragma clang diagnostic pop