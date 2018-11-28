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
#define fore(i, l, r) for (int i = (int)(l); i < (int)(r); i++)
#define forv(i, v) forn(i, v.size())

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

int n;
map<string, int> num;
vector< vector<int> > w;

int getNum(string s) {
    if (num.count(s) == 0) num.insert(mp(s, (int)num.size()));
    return num[s];
}

void solveCase(int tc) {
    cerr << tc << endl;
    printf("Case #%d: ", tc);
    scanf("%d\n", &n);
    num.clear();
    w = vector< vector<int> >(n);
    forn(i, n) {
        string s;
        getline(cin, s);
        istringstream in(s);
        string word;
        while (in >> word) w[i].pb(getNum(word));
    }
    int ans = 1e9;
    int m = num.size();
    forn(mask, 1 << n) {
        if (mask & 1) continue;
        if (((mask >> 1) & 1) == 0) continue;
        vector<int> f(m);
        forn(i, n) {
            int c = (mask >> i) & 1;
            forv(j, w[i]) {
                f[w[i][j]] |= 1 << c;
            }
        }
        int cur = 0;
        forn(i, m) if (f[i] == 3) cur++;
        ans = min(ans, cur);
    }
    cout << ans << endl;
}

int main() {
#ifdef NEREVAR_PROJECT
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
