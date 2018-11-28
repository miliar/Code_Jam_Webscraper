#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <sstream>
#include <complex>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long       li;
typedef vector<li>      vi;
typedef complex<double> pt;
typedef pair<pt, pt>    line;
typedef pair<li, li>    pi;
typedef vector<string>  vs;

#define rep(i,to)       for(li i=0;i<((li)to);++i)
#define foreach(it,set) for(__typeof((set).begin()) it=(set).begin();it!=(set).end();it++)
#define all(v)          v.begin(), v.end()

template <class T> inline void minu(T& x, T y) { x = min(x, y); }
template <class T> inline void maxu(T& x, T y) { x = max(x, y); }

inline li bit(li n){ return 1LL<<n; }
template <class T> ostream& operator<<(ostream& os, vector<T> x){
    foreach(it, x) os << *it << ' ';
    return os;
}

li dx[8] = {1, -1, 0,  0, -1, 1,  1, -1};
li dy[8] = {0,  0, 1, -1, -1, 1, -1,  1};

vector<int> get_assign(int assign, int m, int n) {
    vector<int> ret;
    rep(i, m) {
        ret.push_back(assign % n);
        assign /= n;
    }
    return ret;
}

void solve(int caseNum) {
    int m, n;
    cin >> m >> n;
    vector<string> s(m);
    rep(i, m) cin >> s[i];
    int subset = bit(m);
    vector<int> trie_node(subset, 0);
    rep(mask, subset) {
        set<string> tr;
        rep(i, m) if (bit(i) & mask) {
            rep(l, s[i].length() + 1) {
                tr.insert(s[i].substr(0, l));
            }
        }
        trie_node[mask] = tr.size();
    }

    int pattern = 1;
    rep(i, m) pattern *= n;
    int maxnode = 0, cnt = 0;
    rep(assign, pattern) {
        vector<int> assign_v = get_assign(assign, m, n);
        int nodes = 0;
        vector<int> serv(n);
        rep(i, m) serv[assign_v[i]] += bit(i);
        rep(i, n) nodes += trie_node[serv[i]];
        if (nodes > maxnode) {
            maxnode = nodes;
            cnt = 0;
        }
        if (nodes == maxnode) {
            cnt += 1;
        }
    }
    
    cout << "Case #" << caseNum << ": " << maxnode << " " << cnt << endl;
    return;
}

int main() {
    int n;
    cin >> n;
    rep(i, n) solve(i + 1);
    return 0;
}
