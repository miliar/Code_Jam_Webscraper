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

template<typename T, typename S>
std::ostream& operator << (std::ostream& os, const std::pair<T, S>& p) {
    os << "(" << p.first << ", " << p.second << ")";
    return os;
}

template<typename T>
std::ostream& operator << (std::ostream& os, const std::vector<T>& vector) {
    for (size_t i = 0; i < vector.size(); ++i) {
        os << (i > 0 ? " " : "") << vector[i];
    }
    return os;
}

template<typename T>
std::ostream& operator << (std::ostream& os, const std::vector<std::vector<T>>& vector) {
    for (size_t i = 0; i < vector.size(); ++i) {
        os << vector[i] << std::endl;
    }
    return os;
}


int rem(string s, int p, int mod) {
    int rem = 0;
    forn(i, s.size()) {
        rem = (rem * p + (s[i] - '0')) % mod;
    }
    return rem;
}


string gen(int len) {
    string s(len, '1');
    for (int i = 1; i + 1 < len; ++i) {
        s[i] = static_cast<char>('0' + rand() % 2);
    }
    return s;
}

void solve(int len, int cnt) {
    int kModMax = 100;
    set<string> res;
    while (cnt > 0) {
        string s = gen(len);
        vi mods;
        for (int p = 2; p <= 10; ++p) {
            for (int mod = 2; mod <= kModMax; ++mod) {
                if (rem(s, p, mod) == 0) {
                    mods.push_back(mod);
                    break;
                }
            }
        }
        if (mods.size() == 9 && res.find(s) == res.end()) {
            cout << s << " " << mods << endl;
            --cnt;
            res.insert(s);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    // freopen("C-small-attempt0.in", "r", stdin);
    // freopen("C-small-attempt0.out", "w", stdout);

    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    // auto start = std::chrono::high_resolution_clock::now();
    forn(i, t) {
        int len, cnt;
        cin >> len >> cnt;
        cout << "Case #" << i + 1 << ":\n";
        solve(len, cnt);
    }

    // auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::high_resolution_clock::now() - start).count();
    // cout << "elapsed " << duration << " ms." << endl;

    return 0;
}
