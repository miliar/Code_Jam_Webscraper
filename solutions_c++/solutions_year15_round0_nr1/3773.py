#pragma COMMENT(linker, "/STACK:64000000");

#include <cstring>
#include <iostream>
#include <iomanip>
#include <map>
#include <algorithm>
#include <set>

using namespace std;

int n;
string s;

bool get(int q) {
    for(int i = 0; i < s.size(); i++)
        if (q >= i)
            q += s[i] - '0';
        else return false;
    return true;
}

int solve() {

    int l = 0, r = (int)s.size();

    while (l < r) {
        int m = (l + r) / 2;
        if (get(m))
            r = m;
        else l = m + 1;

    }

    return l;
}

int main() {
//#ifndef LOCAL
//    freopen("input.txt", "rt", stdin);
//    freopen("output.txt", "wt", stdout);
//#endif

    ios::sync_with_stdio(false);

    int t;
    cin >> t;


    for(int T = 1; T <= t; T++) {
        cin >> n >> s;
        cout << "Case #" << T << ": " << solve() << endl;
    }


    return 0;
}