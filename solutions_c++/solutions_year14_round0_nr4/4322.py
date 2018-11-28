#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <complex>
#include <bitset>
#include <limits>
#include <vector>
#include <list>
#include <functional>
#include <deque>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <stack>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;

typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef pair<ll, ll> pll;

const int INF = (int) 1e9;
const ll LINF = (ll) 1e15;
const double PI = 2.0 * acos(0.0);
const double EPS = 1e-8;

#define pb push_back
#define mp make_pair

#define ZERO(x) memset(x,0,sizeof(x))
#define SET(x) memset(x,-1,sizeof(x))
#define SZ(x) (int)x.size()
#define REP(i,b) for(int i=0;i<b;++i)
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin() ;it!=(c).end();++it)
#define ALL(X) X.begin(),X.end()
#define RALL(X) X.rbegin(),X.rend()

int parse(string s) {
    stringstream ss;
    ss << s.substr(2);
    int ans;
    ss >> ans;
    return ans;
}

int main() {
    int T;
    cin >> T;
    FOR(test, 1, T + 1) {
        cout << "Case #" << test << ": ";
        int N;
        cin >> N;
        set<int> a, b;
        REP(i, N) {
            string m;
            cin >> m;
            a.insert(parse(m));
        }
        REP(i, N) {
            string m;
            cin >> m;
            b.insert(parse(m));
        }
        set<int> ca(a), cb(b);
        int x = 0, y = 0;
        REP(i, N) {
            if (*ca.begin() < *cb.begin()) {
                ca.erase(ca.begin());
                cb.erase(*cb.rbegin());
            } else {
                ++x;
                ca.erase(ca.begin());
                cb.erase(cb.begin());
            }
        }
        REP(i, N) {
            set<int>::iterator it = b.upper_bound(*a.begin());
            a.erase(a.begin());
            if (it == b.end()) {
                ++y;
                b.erase(b.begin());
            } else {
                b.erase(it);
            }
        }
        cout << x << " " << y << endl;
    }
    return 0;
}