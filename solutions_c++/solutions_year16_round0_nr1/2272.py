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

string solve(int n) {
    if (n == 0) {
        return "INSOMNIA";
    } else {
        vb v(10, false);
        ll m = 1;
        while (true) {
            ll x = m * n;
            while (x > 0) {
                v[x % 10] = true;
                x /= 10;
            }
            if (find(v.begin(), v.end(), false) == v.end()) {
                break;
            }
            m++;
        }
        return to_string(m * n);
    }
}

void test() {
    forn(i, 1000001) {
        auto start = std::chrono::high_resolution_clock::now();
        cout << i << ": " << solve(i) << endl;
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::high_resolution_clock::now() - start).count();
        if (duration > 100) {
            throw 1;
        }
//        cout << "elapsed " << duration << " ms." << endl;
    }
    exit(0);
}

int main() {
    ios_base::sync_with_stdio(false);
    // freopen("input.txt", "r", stdin);
    //  freopen("output.txt", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
//     freopen("A-small-attempt0.in", "r", stdin);
//     freopen("A-small-attempt0.out", "w", stdout);
//    test();
    int t;
    cin >> t;
    forn(i, t) {
        int n;
        cin >> n;
        cout << "Case #" << i + 1 << ": " << solve(n) << endl;
    }
    return 0;
}
