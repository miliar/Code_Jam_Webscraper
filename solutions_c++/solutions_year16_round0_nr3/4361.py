#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()

#define forn(i,n) for (int i=0; i<int(n); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;


const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;

int n = 16, j = 50;

void solve(){
    map <string, vector <ll> > ans;
    forn(mask, (1<<n)) {
        if (sz(ans) == j) break;
        if ((mask & 1) && (mask & (1<<n-1))) {
            string bin = "";
            vector <ll> b, res;
            for (ll tb = 2; tb<=10; tb++)
                b.pb(1);
            res.assign(9, 0);
            forn(j,n) {
                int dig = (mask & (1<<j)) ? 1 : 0;
                bin += dig ? "1" : "0";
                forn(k,sz(b)) {
                    res[k] += dig * b[k];
                    b[k] *= (2 + k);
                }
            }
            reverse(all(bin));
            vector <ll> proof;
            forn(j,sz(res)) {
                for (ll k=2; k*k <= res[j]; k++) {
                    if (res[j] % k == 0) {
                        proof.pb(k);
                        break;
                    }
                }
            }
            if (sz(proof) == 9)
                ans[bin] = proof;
        }
    }
    puts("Case #1:");
    for (auto it = ans.begin(); it!=ans.end(); it++) {
        cout << it->first << ' ';
        auto proof = it->second;
        forn(i,sz(proof)) {
            cout << proof[i] << ' ';
        }
        cout << endl;
    }
}

int main(){
#ifdef dudkamaster
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
#endif
    solve();
    return 0;
}
