#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <cstring>
#include <fstream>

using namespace std;

vector<string> v;
vector<string> cur;
int n, n2;
bool possible;
vector<int> ord;
bool used[6];

void rec(int pos) {
    if (!possible) return;
    if (pos == n) return;
    int t = ord[pos];
    bool fail = true;
    for(int i=0; i<n; ++i) {
        if (cur[t][i] == '1' && !used[i]) {
            fail = false;
            used[i] = true;
            rec(pos+1);
            used[i] = false;
        }
    }
    if (fail) possible = false;
}

bool check(int mask) {
    cur.clear();
    cur.resize(n, string(n, '0'));
    for(int i=0; i<n2; ++i) {
        int r, c;
        r = i/n;
        c = i%n;
        if (((mask>>i) & 1) == 0 && v[r][c] == '1') return false;
        if ((mask>>i) & 1) cur[r][c] = '1';
    }
    ord.clear();
    for(int i=0; i<n; ++i) {
        ord.push_back(i);
    }
    possible = true;
    do {
        memset(used, 0, sizeof(used));
        rec(0);
    } while (possible && next_permutation(ord.begin(), ord.end()));
    return possible;
}

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int T, NT, i, j;
    cin>>NT;
    int res;
    for(T=1; T<=NT; ++T) {
        cin>>n;
        res = -1;
        n2 = n*n;
        v.clear();
        v.resize(n);
        for(i=0; i<n; ++i) {
            cin>>v[i];
        }
        for(i=0; i<(1<<n2); ++i) {
            if (check(i)) {
                if (res == -1) res = __builtin_popcount(i);
                else res = min(res, __builtin_popcount(i));
            }
        }
        for(i=0; i<n; ++i) {
            for(j=0; j<n; ++j) {
                res -= (v[i][j] == '1');
            }
        }
        cout<<"Case #"<<T<<": "<<res<<endl;
    }

    return 0;
}


