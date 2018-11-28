
#include <bits/stdc++.h>
#define err(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)

typedef long long ll;
using namespace std;

const int dd = (int)1001;

int A[21];

int main() {
    int t;
    cin >> t;

    for (int test = 1; test <= t; test++) {


        string s;
        cin >> s;
        int k;
        cin >> k;

        int n = (int)s.size();
        int ans = 0, ok = 1;

        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                if (i + k > n) {
                    ok = 0;
                    break;
                }
                ans++;
                for (int j = i; j < i + k; j++) {
                    s[j] = (s[j] == '+' ? '-' : '+');
                }
            }
        }

        if (ok) {
            cout << "Case #" << test << ": " << ans << "\n";
        } else {
            cout << "Case #" << test << ": " << "IMPOSSIBLE" << "\n";
        }
    }
    return 0;
}

