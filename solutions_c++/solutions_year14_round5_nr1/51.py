#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iomanip>

using namespace std;
 
#define debug(x) cerr << "DEBUG: " << #x << " = " << x << endl
#define forn(i, n) for(int i = 0; i < (n); ++i)
#define all(x) x.begin(), x.end()
#define mp make_pair
#define pb push_back

template <typename T> inline void mn(T& x, const T& y) { if (y < x) x = y; }
template <typename T> inline void mx(T& x, const T& y) { if (x < y) x = y; }
template <typename T> inline int sz(const T& x) { return (int) x.size(); }

inline long long SUM(int l, int r, const vector<long long>& sums) {
    return sums[r] - sums[l];
}

int n;

    long long s[3];

inline long long f(int l, int r, const vector<long long>& sums) {
    s[0] = SUM(0, l, sums);
    s[1] = SUM(l, r + 1, sums);
    s[2] = SUM(r + 1, n, sums);
    return *max_element(s, s + 3);
}

int main() {
    // freopen("in.txt", "r", stdin);
    freopen("A-large.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    ios_base::sync_with_stdio(false);

    int nTests;
    cin >> nTests;
    forn (iTest, nTests) {
        cout << "Case #" << (iTest + 1) << ": ";
        long long p, q, r, s;
        cin >> n >> p >> q >> r >> s;

        vector<int> a(n);
        vector<long long> sums(n + 1);
        sums[0] = 0;
        forn (i, n) {
            a[i] = (i * p + q) % r + s;
            sums[i + 1] = sums[i] + a[i];
        }


        long long score = numeric_limits<long long>::max();

        long long other = sums[n];

        for (int r = 0; r < n; ++r) {
            
            other -= a[r];

            int index = lower_bound(sums.begin(), sums.begin() + r + 1, sums[r + 1] / 2) - sums.begin();
            int L = max(0, index - 10);
            int R = min(r, index + 10);
            for (int i = L; i <= R; ++i) {
                mn(score, f(i, r, sums));
            }

            index = lower_bound(sums.begin(), sums.begin() + r + 1, other / 2) - sums.begin();
            L = max(0, index - 10);
            R = min(r, index + 10);
            for (int i = L; i <= R; ++i) {
                mn(score, f(i, r, sums));
            }

            // for (int i = 0; i <= r; ++i) {
                // mn(score, f(i, r, sums));
            // }
        }
        double ans = 1.0 * score / sums.back();
        cout << fixed << setprecision(15) << 1 - ans << endl;
    }    

    return 0;
}