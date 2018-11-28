#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstdlib>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>

#define mp make_pair

using namespace std;

typedef long long ll;

vector<vector<int> > v;
map<string, int> m;
int n;
int cc;

int calc(int mask) {
    vector<int> s(cc, 0);
    for(int i=0; i<n; ++i) {
        int cur = (1<<((mask>>i) & 1));
        for(int j=0; j<v[i].size(); ++j) {
            s[v[i][j]] |= cur;
        }
    }
    int res = 0;
    for(int i=0; i<cc; ++i) {
        res += (s[i] == 3);
    }
    return res;
}

int main() {
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    int T, NT;
    cin>>NT;
    int i, j;
    for(T=1; T<=NT; ++T) {
        cin>>n;
        v.clear();
        v.resize(n);
        m.clear();
        cc = 0;
        string line;
        getline(cin, line); // line with N
        for(i=0; i<n; ++i) {
            getline(cin, line);
            istringstream ss(line);
            string s;
            while(ss>>s) {
                if (!m.count(s)) {
                    m[s] = cc++;
                }
                v[i].push_back(m[s]);
            }
        }
        int res = 1000000;
        for(i=0; i<(1<<n); ++i) {
            if ((i & 3) != 2) continue;
            res = min(res, calc(i));
        }
        printf("Case #%d: %d\n", T, res);
    }
    return 0;
}

