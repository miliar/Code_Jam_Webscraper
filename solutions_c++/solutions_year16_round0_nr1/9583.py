
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef int INT;
#define int ll

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

    qfor (I, 0, T) {
        int n;
        cin >> n;
        int m = n;

        bool used[10];
        fill (used, used + 10, false);

        for (int i = 0; i < 105; ++i) {
            for (c : to_string(m)) {
                used[c - '0'] = true;
            }
            if (find(used, used + 10, false) == used + 10) {
                break;
            }
            m += n;
        }

        cout << "Case #" << I + 1 << ": ";
        if (find(used, used + 10, false) != used + 10) {
            cout << "INSOMNIA" << endl;
        } else {
            cout << m << endl;
        }
    }
}
