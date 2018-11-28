#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <iomanip>
#include <queue>
#include <utility>
#include <stack>
#include <ctime>

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define forn(i,n) for (i = 0; i < n; i++)

using namespace std;

typedef pair <int, int> pii;
typedef long double ld;
typedef long long ll;

const ld EPS = 1e-9;
const int INF = (int) 1e9;
const int N = (int) 1e3 + 5;
const ll M = (int) 1e9 + 7;

string print_mask(int mask) {
    string res = "";
    while (mask) {
        if (mask % 2)
            res += '1';
        else
            res += '0';
        mask /= 2;
    }
    reverse(res.begin(), res.end());
    return res;
}

bool bit(int mask, int i) {
    return (1 << i) & mask;
}

int divisor(ll x) {
    ll i = 2;
    while (i * i <= x) {
        if (x % i == 0)
            return i;
        i++;
    }
    return -1;
}

int answer(int mask, int base, int n) {
    ll x = 0;
    ll pw = 1;
    for (int i = 0; i < n; i++, pw *= base)
        x += 1ll * bit(mask, i) * pw;
    return divisor(x);
}

int to_mask(vector <int> &v) {
    int res = 0, n = v.size();
    for (int i = 0 ; i < n; i++)
        res += (1 << (n - i - 1)) * v[i];
    return res;
}

void solve(int n, int m) {
    for (int i1 = 1; i1 < n - 1; i1++)
        for (int i2 = i1 + 1; i2 < n - 1; i2++)
            for (int i3 = i2 + 1; i3 < n - 1; i3++)
                for (int i4 = i3 + 1; i4 < n - 1; i4++)
                    if ((4 + i1 % 2 + i2 % 2 + i3 % 2 + i4 % 2) % 3 == 0 && (4 + 5 * (i1 % 2) + 5 * (i2 % 2) + 5 * (i3 % 2) + 5 * (i4 % 2)) % 7 == 0) {
                        cout << 1;

                        for (int i = n - 2; i; i--)
                            cout << (i == i1 || i == i2 || i == i3 || i == i4 ? 1 : 0);
                        cout << "1 ";
                        cout << "3 2 3 2 7 2 3 2 3\n";
                        m--;
                        if (!m)
                            exit(0);
                    }
}

int main() {
    //freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n, m;
        cin >> n >> m;
        cout << "Case #" << t + 1 << ":\n";
        solve(n, m);

    }
	return 0;
}
