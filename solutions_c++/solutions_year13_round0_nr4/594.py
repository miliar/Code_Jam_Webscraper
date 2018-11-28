#include <iostream>
#include <sstream>

#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <string>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>

#include <algorithm>
#include <numeric>

#define foreach(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define sqr(x) ((x) * (x))
#define len(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define pbk pop_back
#define mp make_pair
#define fs first
#define sc second
#define endl '\n'
#ifdef CUTEBMAING
#include "cutedebug.h"
#else
#define debug(x) ({})
#endif

using namespace std;

typedef long long int64;
typedef unsigned long long lint;
typedef long double ld;

const int inf = ((1 << 30) - 1);
const int64 linf = ((1ll << 62) - 1);

const char* fin = "input.txt";
const char* fout = "output.txt";
const int cmax = 1 << 20;

int k, n;
bool u[cmax];
vector<int> startKeys;
vector<int> sbKey;
vector<vector<int> > keys;
vector<map<int, int> > leftKeys;
vector<int> ans;

bool dfs(int mask){
    if (u[mask])
        return false;
    if (mask == (1 << n) - 1)
        return true;
    u[mask] = true;
    map<int, int> &curKeys = leftKeys[mask];
    for (int i = 0; i < k; i++)
        ++curKeys[startKeys[i]];
    for (int i = 0; i < n; i++)
        if (mask & (1 << i)){
            foreach(j, keys[i])
                ++curKeys[*j];
            --curKeys[sbKey[i]];
        }
    for (int i = 0; i < n; i++)
        if (!(mask & (1 << i)) && curKeys[sbKey[i]] > 0 && dfs(mask | (1 << i))){
            ans.pb(i);
            return true;
        }
    return false;
}

void solve(){
    ans.clear();
    memset(u, 0, sizeof(u));
    cin >> k >> n;
    startKeys.assign(k, 0);
    for (int i = 0; i < k; i++)
        cin >> startKeys[i];
    keys.assign(n, vector<int>());
    sbKey.assign(n, 0);
    for (int i = 0; i < n; i++){
        int t; cin >> sbKey[i] >> t;
        keys[i].assign(t, 0);
        for (int j = 0; j < t; j++)
            cin >> keys[i][j];
    }
    leftKeys.assign(cmax, map<int, int>());
    if (!dfs(0))
        puts("IMPOSSIBLE");
    else{
        reverse(all(ans));
        foreach(i, ans)
            printf("%d ", *i + 1);
        printf("\n");
    }
}

int main(){
    #if !defined STRESS && defined CUTEBMAING
    assert(freopen(fin, "r", stdin));
    assert(freopen(fout, "w", stdout));
    #endif
    int t; cin >> t;
    for (int i = 0; i < t; i++){
        double begin = clock();
        fprintf(stderr, "Starting solving case %d\n", i + 1);
        printf("Case #%d: ", i + 1);
        solve();
        fprintf(stderr, "Case %d has been successfully solved. ИНФА 100%%\n", i + 1);
        fprintf(stderr, "Time elapsed: %.10f\n", (clock() - begin) / CLOCKS_PER_SEC);
    }
    return 0;
}
