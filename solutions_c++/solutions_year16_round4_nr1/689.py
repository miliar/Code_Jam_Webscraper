#include <iostream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstdio>
#include <cstring>
using namespace std;

bool check(const string &s)
{
    if (s.length() == 1) return true;

    string t;
    for (int i = 0; i < s.size(); i+=2) {
        char a = s[i];
        char b = s[i + 1];

        if (a == b) return false;

        t +=
            a == 'R' && b == 'S' ? 'R' :
            a == 'R' && b == 'P' ? 'P' :
            a == 'S' && b == 'R' ? 'R' :
            a == 'S' && b == 'P' ? 'S' :
            a == 'P' && b == 'R' ? 'P' :
            a == 'P' && b == 'S' ? 'S' : '*';
    }

    return check(t);
}

void solve()
{
    int n, r, p, s;
    cin >> n >> r >> p >> s;

    string ord;
    ord += string(r, 'R');
    ord += string(p, 'P');
    ord += string(s, 'S');

    sort(ord.begin(), ord.end());

    do {
        if (check(ord)) {
            cout << ord << endl;
            return;
        }
    } while(next_permutation(ord.begin(), ord.end()));

    cout << "IMPOSSIBLE" << endl;
}

int main()
{
    int t; cin >> t;
    for (int cn = 1; cn <= t; cn++) {
        cout << "Case #" << cn << ": ";
        solve();
    }

    return 0;
}
