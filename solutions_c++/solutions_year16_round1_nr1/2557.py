#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <climits>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define sqr(x) ((x) * (x))
#define sz(v) (int)(v).size()
#define all(v) (v).begin(), (v).end()

typedef long long ll;
typedef long double ld;
typedef vector <int> vi;
typedef pair <int, int> pii;

void solve(int test) {
    cout << "Case #" << test << ": ";
    string s;
    cin >> s;
    vector <char> res;
    for (int i = 0; i < sz(s); i++) {
        if (sz(res) == 0) {
            res.pb(s[i]);
            continue;
        }
        if (res[0] > s[i]) {
            res.pb(s[i]);
        } else {
            res.insert(res.begin(), s[i]);
        }
    }
    for (char ch : res) {
        cout << ch;
    }
    cout << "\n";
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("/Users/nurlan/Dropbox/Programming/contest/contest/input", "r", stdin);
    freopen("/Users/nurlan/Dropbox/Programming/contest/contest/output", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        solve(test);
    }
    return 0;
}