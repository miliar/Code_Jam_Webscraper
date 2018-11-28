#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <unordered_set>
#endif

using namespace std;

#define ALL(x) (x).begin(), (x).end()
#define EACH(itr,c) for(__typeof((c).begin()) itr=(c).begin(); itr!=(c).end(); itr++)  
#define FOR(i,b,e) for (int i=(int)(b); i<(int)(e); i++)
#define MP(x,y) make_pair(x,y)
#define REP(i,n) for(int i=0; i<(int)(n); i++)

int M, N;
string s[8];
int a[8];

struct node {
    node *nxt[26];
    node() {
        REP (i, 26)
            nxt[i] = NULL;
    }
};

node pool [10000];
node *pptr;

void insert(node *p, const string str, int pos) {
    if (pos >= (int)str.length())
        return;
    
    int v = str[pos] - 'A';
    if (!p->nxt[v]) {
        REP (i, 26)
            pptr->nxt[i] = NULL;
        p->nxt[v] = pptr++;
    }
    insert(p->nxt[v], str, pos+1);
}

int calc(int v) {
    pptr = pool;
    node root;

    REP (i, M) {
        if (a[i] != v) continue;
        insert(&root, s[i], 0);
    }
    
    return pptr - pool;
}

int doit() {
    int ret = 0;
    REP (i, N)
        ret += calc(i);
    return ret + N;
}

void solve() {
    cin >> M >> N;
    REP (i, M) cin >> s[i];

    int x = -1;
    int SZ = 1;
    REP (i, M) SZ *= N;
    REP (mask, SZ) {
        int tmp = mask;
        REP (i, M) {
            a[i] = tmp % N;
            tmp /= N;
        }
        
        int cnt[4] = {0};
        REP (i, M) cnt[a[i]]++;
        bool ck = true;
        REP (i, N) if (cnt[i] == 0) ck = false;
        if (!ck) continue;  // empty server
        
        x = max(x, doit());
    }

    int y = 0;
    REP (mask, SZ) {
        int tmp = mask;
        REP (i, M) {
            a[i] = tmp % N;
            tmp /= N;
        }
        
        int cnt[4] = {};
        REP (i, M) cnt[a[i]]++;
        bool ck = true;
        REP (i, N) if (cnt[i] == 0) ck = false;
        if (!ck) continue;  // empty server
        if (doit() == x)
            ++y;
    }

    cout << x << " " << y << endl;

}

int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    REP (i, T) {
        cerr << "Case #" << i+1 << ": " << endl;
        cout << "Case #" << i+1 << ": ";
        solve();
    }

    return 0;
}
