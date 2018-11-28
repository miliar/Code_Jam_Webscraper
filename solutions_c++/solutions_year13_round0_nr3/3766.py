#include <iostream>
#include <string>
#include <cstdio>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <stack>
#include <cctype>
#include <cstdlib>
#include <bitset>
#include <utility>
#include <cstring>

using namespace std;

const long double EPS = 1e-8;
const long double PI = 3.1415926535897932384626433832795;
const long double E = 2.7182818284;
const int INF = 1000000000;

typedef long long ll;
typedef long double ld;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define pb push_back
#define all(a) a.begin(), a.end()
#define mp make_pair;
#define X first
#define Y second

vector <long long> res;

int check(long long k, int n) {
    char buf[20];
    int f = 0;
    sprintf(buf, "%lld", k);
    for (int i = 0; i < n / 2; i++) {
        if (buf[i] != buf[n - i - 1]) {
            f = 1;
            break;
        }
    }
    if (!f) return 1;
    return 0;
}

int main(void)
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, i;
    cin >> t;
    int len1 = 1;
    int len2 = 1;
    int n1 = 1;
    long long n2 = 1;
    for (int i = 1; i <= 1000001; i++) {
        if (i >= 10 * n1) {
            n1 *= 10;
            len1++;
        }
        if (1LL * i * i >= 10LL * n2) {
            n2 *= 10LL;
            len2++;
        }
        if (check(i, len1) && check(1LL * i * i, len2) ) res.pb(1LL * i * i);
    }
    forn(i, t) {
        long long a, b;
        cin >> a >> b;
        int ans = 0;
        for (int j = 0; j < res.size(); j++) {
            if (res[j] > b) break;
            if (res[j] < a) continue;
            ans++;
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    return 0;
}
