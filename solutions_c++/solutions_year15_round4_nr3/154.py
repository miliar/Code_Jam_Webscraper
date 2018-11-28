#include <cassert>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <string>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <sstream>

using namespace std;

#define FOR(a, b) for (int a = 0; a < (b); ++a)
#define clr(a) memset(a, 0, sizeof(a))
#define pb(i) push_back(i)
#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)
#ifdef LOCAL
#define debug(a) cerr << #a << ": " << a << '\n';
#else
#define debug(a)
#endif

typedef long long ll;
typedef long double ldb;

const int INF = 1e9;
const ldb EPS = 1e-8;
const ldb PI = acos(-1.0);
const int MAXN = 210;
const int MAXW = 1e4 + 100;

set<int> w[MAXN];
bool ise[MAXW];
bool isf[MAXW];

int n;

int fr = 0;

int ans;

int rec(int st, int ans) {
    if (st == n) {
        return ans;
    }
    bool was[11];
    int c = 0;
    int nans = ans;
    for (auto i : w[st]) {
        was[c] = ise[i];
        ise[i] = true;
        if (!was[c] && isf[i])
            nans++;
        c++;
    }
    int res = rec(st + 1, nans);
    c = 0;
    for (auto i : w[st]) {
        ise[i] = was[c];
        c++;
    }
    //cerr << st << " 1 " << res << '\n';

    c = 0;
    nans = ans;
    for (auto i : w[st]) {
        was[c] = isf[i];
        isf[i] = true;
        if (!was[c] && ise[i])
            nans++;
        c++;
    }
    res = min(res, rec(st + 1, nans));
//    cerr << st << " 2 " << res << '\n';
    c = 0;
    for (auto i : w[st]) {
        isf[i] = was[c];
        c++;
    }
    return res;


}

int main() {
#ifdef LOCAL
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    //freopen("", "w", stderr);
#endif
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cin >> n >> ws;
  //      cerr << n << '\n';
        FOR(i, n)
            w[i].clear();
        map<string, int> words;
        fr = 0;
        FOR(i, n) {
            string buf;
            getline(cin, buf);
            stringstream ss(buf);
//            cerr << buf << '\n';
            cin >> ws;
            string s;
            while(ss >> s) {
                int nm;
                if (words.count(s) == 0)
                    words[s] = fr++;
                nm = words[s];
                w[i].insert(nm);
            }
        }
        /*
        for (auto t : words) {
            cerr << t.first << ' ' << t.second << '\n';
        }*/
        clr(ise);
        clr(isf);
        for (auto i : w[0])
            ise[i] = true;
        for (auto i : w[1])
            isf[i] = true;
        ans = 0;
        FOR(i, fr)
            if (ise[i] && isf[i])
                ans++;
        cout << "Case #" << test << ": ";
        cout << rec(2, ans) << '\n';

            
    }
    return 0;
}

