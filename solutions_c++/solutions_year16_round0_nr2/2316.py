#include <climits>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define mp make_pair
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<char> vc;
typedef vector<vc> vvc;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef pair<int, int> Point;
typedef vector<Point> vp;
typedef vector<vp> vvp;

bool DBG = false;

int solve(const string& s) {
    int pos = 0, res = 0;
    while (pos < s.length()) {
        int plus_len = 0;
        while (pos < s.length() && s[pos] == '+') {
            ++pos;
            ++plus_len;
        }
        int minus_len = 0;
        while (pos < s.length() && s[pos] == '-') {
            ++pos;
            ++minus_len;
        }
        if (minus_len != 0) {
            if (plus_len != 0) {
                ++res;
            }
            ++res;
        }
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
      
    // freopen("B-small-attempt0.in", "r", stdin);
    // freopen("B-small-attempt0.out", "w", stdout);

    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    forn(i, t) {
        string s;
        cin >> s;
        cout << "Case #" << i + 1 << ": " << solve(s) << endl;
    }
    return 0;
}
