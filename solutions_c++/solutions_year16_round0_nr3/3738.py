#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <iterator>
#include <queue>
#include <algorithm>

#define mp make_pair
#define pb push_back
#define x first
#define y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<int, pii> piii;
typedef pair<ll, ll> pll;
typedef pair<ld, ld> point;
typedef pair<pll, pll> seg;
typedef vector<int> lnum;

const int N = (int)(2e5) + 7;
const int M = (int)(1e6) + 7;
const int K = (int)(1e4) + 7;
const int BLOCK_SIZE = 320;
const ld eps = 1e-9;
const ll INF = (ll)(1e9) + 7;
const ll MOD = (ll)(1e9) + 7;

string tostr(int x, int n) {
    string res = "";
    for (int i = 0; i < n; ++i) {
        int q = x % 2;
        x /= 2;
        if (q)
            res = "1" + res;
        else
            res = "0" + res;
    }
    return res;
}

ll todec(string s, int base) {
    ll res = 0;
    for (int i = 0; i < s.size(); ++i) {
        res *= base;
        res += (int)(s[i]) - '0';
    }
    return res;
}

int simple(ll x) {
    ll i = 2;
    while (i * i <= x) {
        if (x % i == 0)
            return i;
        ++i;
    }
    return 1;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int ttt;
    cin >> ttt;
    for (int iii = 1; iii <= ttt; ++iii) {
        printf("Case #%d:\n", iii);
        int n, k;
        cin >> n >> k;
        int count = 0;
        n -= 2;
        for (int i = 0; i < (1 << n); ++i) {
            if (count == k)
                break;
            string s = "1" + tostr(i, n) + "1";
            int a[11];
            int f = 0;
            for (int j = 2; j <= 10; ++j) {
                a[j] = simple(todec(s, j));
                if (a[j] == 1) {
                    f = 1;
                    break;
                }
            }
            if (!f) {
                ++count;
                cout << s;
                for (int j = 2; j <= 10; ++j)
                    cout << " " << a[j];
                cout << endl;
            }
        }
    }
    return 0;
}
