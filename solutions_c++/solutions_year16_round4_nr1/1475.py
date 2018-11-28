#include <cstdio>
#include <sstream>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

std::string work(int n, int r, int p, int s, int depth)
{
    //cout << n << p << r << s << endl;;
    if (n == 0) {
        if (p > 0) return "P";
        if (r > 0) return "R";
        if (s > 0) return "S";
    }

    int x, y, z; // PR, RS, SP
    x = (1 << (n - 1)) - s;
    y = (1 << (n - 1)) - p;
    z = (1 << (n - 1)) - r;
    if (x < 0 || y < 0 || z < 0) return "";

    string last = work(n - 1, y, x, z, depth + 1);
    //cout << last << endl;
    if (last.size() == 0) return last;
    stringstream ss;
    for (char c : last) {
        if (depth % 3 == 0) {
            if (c == 'P') ss << "PR";
            if (c == 'R') ss << "RS";
            if (c == 'S') ss << "PS";
        } else if (depth % 3 == 1) {
            if (c == 'P') ss << "PR";
            if (c == 'R') ss << "SR";
            if (c == 'S') ss << "PS";
        } else {
            if (c == 'P') ss << "PR";
            if (c == 'R') ss << "SR";
            if (c == 'S') ss << "SP";
        }
    }
    return ss.str();
}

/*
P PR PRRS
R RS PSRS
S PS PRPS
*/

void solve() {
    int N, R, P, S;
    cin >> N >> R >> P >> S;

    string ans = work(N, R, P, S, 0);
    if (ans.size() == 0)
        cout << "IMPOSSIBLE" << endl;
    else
        cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cout << "Case #" << testcase << ": ";
        solve();
    }
    return 0;
}
