#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string.h>
#include <queue>
#include <cstdio>
#include <cassert>
#include <deque>
#include <stack>
#include <utility>
#include <numeric>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

const int MAXN = 10;

vector<double> a, b;
int n;
int z[1 << MAXN][1 << MAXN];

int calc(int m1, int m2, bool cheat) {
    if (m1 == 0) return 0;
    if (z[m1][m2] != -1) return z[m1][m2];
    int ans = 0;
    forn(i, n) {
        if (m1 & (1 << i)) {			
            int j = 0;
            while (j < n && (b[j] < a[i] || (m2 & (1 << j)) == 0)) j++;
            if (j < n) {
                ans = max(ans, calc(m1 ^ (1 << i), m2 ^ (1 << j), cheat));
            } else {
                j = 0;
                while ((m2 & (1 << j)) == 0) j++;
                ans = max(ans, 1 + calc(m1 ^ (1 << i), m2 ^ (1 << j), cheat));
            }			
        }
    }
    if (cheat) {
        int i = 0;
        while ((m1 & (1 << i)) == 0) i++;
        int j = n - 1;
        while ((m2 & (1 << j)) == 0) j--;
        ans = max(ans, calc(m1 ^ (1 << i), m2 ^ (1 << j), cheat));
        j = 0;
        while ((m2 & (1 << j)) == 0) j++;
        for (i = 0; i < n; i++) {
            if (m1 & (1 << i)) {
                if (a[i] > b[j]) {
                    ans = max(ans, 1 + calc(m1 ^ (1 << i), m2 ^ (1 << j), cheat));
                }
            }    
        }
    }
    return z[m1][m2] = ans;
}

void solve(int tc) {
    cout << "Case #" << tc << ": ";
	cin >> n;
    a = vector<double>(n);
    b = vector<double>(n);
    forn(i, n) cin >> a[i];
    forn(i, n) cin >> b[i];
    sort(all(a));
    sort(all(b));
    memset(z, 255, sizeof(z));
    cout << calc((1 << n) - 1, (1 << n) - 1, true) << " ";
    memset(z, 255, sizeof(z));
    cout << calc((1 << n) - 1, (1 << n) - 1, false) << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    forn(i, tc) solve(i + 1);
    return 0;
}
