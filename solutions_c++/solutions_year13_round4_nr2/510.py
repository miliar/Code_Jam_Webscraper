 #include <set>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <utility>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#define INF 2e9
#define pb push_back
#define mp make_pair
#define forn(i,n) for (int i = 0; i < n; i++)
#define MAXN 100

using namespace std;

typedef long long ll;

int tests;
ll n, p;
ll pw[MAXN];

bool check1(ll m) {
    ll res = 0, i = 1, l = 0;

    while (res < m) {
        l++;
        res += pw[i];
        i++;
    }
    ll place = pw[n] - pw[n - l] + 1;
    //cout << m << " pl " << place << endl;
    return place <= p;
}

bool check2(ll m) {
    ll res = 1, i = 1, w = 0;
    while (m + 2 * res - 1 < pw[n]) {
        w++;
        res = pw[i];
        i++;
    }
    ll place = pw[n - w];
    //if (m == 5) {
    //    cout << "%" << place << " w " << w << endl;
   // }
    return place <= p;
}

ll bs1() {
    ll l = 0, r = pw[n] - 1;
    ll m;
    while (l < r) {
        m = (l + r) / 2;
        if (check1(m)) {
            l = m + 1;
        } else {
            r = m;
        }
    }
    if (!check1(l)) {
        l--;
    }
    return l;
}

ll bs2()
{
    ll l = 0, r = pw[n] - 1;
    ll m;
    while (l < r) {
        m = (l + r) / 2;
        if (check2(m)) {
            l = m + 1;
        } else {
            r = m;
        }
    }
    if (!check2(l)) {
        l--;
    }
    return l;


}
void solve(ll it) {
    cout << "Case #" << it << ": " << bs1() << " " << bs2() << endl;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    pw[0] = 1;
    for (int i = 1; i < MAXN; i++) {
        pw[i] = pw[i - 1] * 2;
    }
    cin >> tests;
    forn (it, tests) {
        cin >> n >> p;
        solve(it + 1);

    }
    return 0;
}
