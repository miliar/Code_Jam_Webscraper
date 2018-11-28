// for small dataset
#include <iostream>
#include <string>
#include <array>
#include <algorithm>
using namespace std;
#define rep(i,n) for (int i = 0; i < int(n); i++)

typedef array<int, 4> Q;

Q one = { 1, 0, 0, 0 },
    I = { 0, 1, 0, 0 },
    J = { 0, 0, 1, 0 },
    K = { 0, 0, 0, 1 };

Q toQ(char c) {
    if (c == 'i') return I;
    if (c == 'j') return J;
    if (c == 'k') return K;
}
Q operator*(Q const& a, Q const& b) {
    return { a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3],
            a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2],
            a[0]*b[2]+a[2]*b[0]+a[3]*b[1]-a[1]*b[3],
            a[0]*b[3]+a[3]*b[0]+a[1]*b[2]-a[2]*b[1] };
}

int T;
int main() {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int X, L;
        string s0, s;
        cin >> L >> X >> s0;
        rep (i,X) s += s0;
        bool result = true;

        Q p = one;
        rep (i,s.size()) p = p * toQ(s[i]);
        if (p != Q{ -1, 0, 0, 0 }) {
            result = false;
        }

        int i1 = 0;
        p = { 1, 0, 0, 0 };
        for ( ; i1 < (int)s.size(); i1++) {
            p = p * toQ(s[i1]);
            if (p == I) break;
        }
        if (i1 == s.size()-1) result = false;

        reverse(s.begin(), s.end());

        int i3 = 0;
        p = { 1, 0, 0, 0 };
        for ( ; i3 < (int)s.size(); i3++) {
            p = toQ(s[i3]) * p;
            if (p == K) break;
        }
        if (i3 == s.size()-1) result = false;
        i3 = s.size()-1-i3;
        if (!(i1+1 < i3)) result = false;

        cout << "Case #" << t << ": " << (result ? "YES" : "NO") << endl;
    }
}
