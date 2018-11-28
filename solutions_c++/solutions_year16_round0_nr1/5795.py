#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;
using ll = long long;

#define all(c) (c).begin(), (c).end()
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
#define fr first
#define sc second

const ll INF = 1e9;
const ll MOD = 1e9 + 7;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int N;

void insert(ll n, set<int> &s) {
    while (n) {
        s.insert(n % 10);
        n /= 10;
    }
}

void solve() {
    if (N == 0) {
        printf("INSOMNIA\n");
        return;
    }
    cerr << N <<endl;
    ll n = N;
    set<int> s;
    while (1) {
        insert(n, s);
        if (s.size() == 10) break;
        n += N;
    }
    printf("%lld\n", n);
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cin >> N;
        printf("Case #%d: ", i+1);
        solve();
    }
    return 0;
}
