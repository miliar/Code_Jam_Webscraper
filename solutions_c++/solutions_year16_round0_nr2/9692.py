
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef int INT;
// #define int ll

typedef pair<int, int> pii;
#define one first
#define two second

#define isize(v) static_cast<int>(v.size())

#define qfor(i, a, b) for (int i = static_cast<int>(a); i < static_cast<int>(b); ++i)
#define fori(n) qfor (i, 0, n)
#define forj(n) qfor (j, 0, n)

void rev(string &s, int n) {
    fori (n) {
        if (s[i] == '-') {
            s[i] = '+';
        } else {
            s[i] = '-';
        }
    }
    reverse(s.begin(), s.begin() + n);
}

INT main() {
    int T;
    cin >> T;

    string s;
    qfor (I, 0, T) {
        cin >> s;

        int ans = 0;

        while (1) {
            int p = find(s.begin(), s.end(), '-') - s.begin();
            if (p == isize(s)) {
                break;
            }
            if (p != 0) {
                ++ans;
                rev(s, p);
            }

            p = s.rend() - find(s.rbegin(), s.rend(), '-');
            ++ans;
            rev(s, p);
        }

        cout << "Case #" << I + 1 << ": " << ans << endl;
    }
}
