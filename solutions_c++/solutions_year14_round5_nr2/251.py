#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

int p,q,n;
int h[101], g[101];
int res;
map<vector<int>, int> dp;

int rec(vector<int> &v) {
    int tot = 0;
    for (int i=0; i<n; i++) if (v[i]>0) tot += g[i];

    if (tot==0) {
        return 0;
    }
    if (dp.find(v)!=dp.end()) return dp[v];

    tot = 0;

    for (int i=0; i<n; i++) if (v[i]>0) {
        v[i] -= p;
        int tmp = 0;
        if (v[i]<=0) tmp += g[i];
        bool done = 0;
        for (int j=0; j<n; j++) if (v[j]>0) {
            v[j] -= q;
            tot = max(rec(v)+tmp, tot);
            v[j] += q;
            done = 1;
            break;
        }
        if (!done) tot = max(tot, tmp);
        v[i] += p;
    }
    for (int j=0; j<n; j++) if (v[j]>0) {
        v[j] -= q;
        tot = max(tot, rec(v));
        v[j] += q;
        break;
    }

    dp[v] = tot;
    return tot;
}

int main() {

	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int t=1; t<=tt; t++) {
        cin>>p>>q>>n;
        for (int i=0; i<n; i++) cin>>h[i]>>g[i];

        vector<int> v(n,0);
        for (int i=0; i<n; i++) v[i] = h[i];
        res = 0;
        dp.clear();
        res = rec(v);
        printf("Case #%d: %d\n", t, res);
    }

	return 0;
}
