#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long long LL;

const int mod = 1000000007;
const int INF = mod;

void flip(string& s, int pos) {
    for (int i = 0; i <= pos; i++) {
        s[i] = (s[i] == '+') ? '-' : '+';
    }
    reverse(s.begin(), s.begin() + pos + 1);
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for (int cn = 1; cn <= T; cn++) {
        cout << "Case #" << cn << ": ";
        string s;
        cin >> s;
        int r = 0;
        for (int i = (int)s.length() - 1; i >= 0; i--) {
            if (s[i] == '-') {
                if (s[0] == '-') {
                    flip(s, i);
                    r++;
                } else {
                    int j = 0;
                    for (; s[j] == '+'; j++);
                    flip(s, j - 1);
                    flip(s, i);
                    r += 2;
                }
            }
        }
        cout << r << endl;
    }
    return 0;
}
