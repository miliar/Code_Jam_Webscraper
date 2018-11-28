#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <map>
#include <utility>
#include <set>
#include <memory>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>

using namespace std;

#define rep(i,b,e) for(int i=b;i<e;++i)
#define mp make_pair
#define pb push_back
#define all(c) (c).begin(),(c).end()

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

static const ll Zp = 1000000009;
static const double EPS = 1e-9;

ll gcd(ll x, ll y) {return x ? gcd(y%x,x) : y;}

int T;
int D;
map<string, int> DP;

int solve(string ds){
    auto fi = DP.find(ds);
    if (fi != DP.end()) {
        return fi->second;
    }

    int mx = ds[ds.size()-1] - '0';
    int r = mx;
    if (mx == 1) return 1;

    string dn;
    //================================
    rep(i,0,ds.size()) {
        if (ds[i] != '1') {
            dn.append(1, ds[i]-1);
        }
    }
    sort(all(dn));
    r = min(r, solve(dn) + 1);
    //================================

    //================================
    rep(i,1,mx) {
        dn = ds;
        dn[dn.size()-1] = dn[dn.size()-1]-i;
        dn.append(1, i+'0');
        sort(all(dn));
        r = min(r, solve(dn) + 1);
    }
    //================================

    DP[ds] = r;

    return r;
}

int main(int argc, char *argv[]) {
    cin>>T;
    for(int t=1;t<=T;++t) {
        cin>>D;
        DP.clear();
        string ds;
        rep(i,0,D) {
            int d;
            cin >> d;
            ds.append(1, '0'+d);
        }
        sort(all(ds));
        cout<<"Case #"<<t<<": "<<solve(ds)<<endl;
    }
    return 0;
}
