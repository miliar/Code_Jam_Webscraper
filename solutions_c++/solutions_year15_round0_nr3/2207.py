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
#define pb push_back

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

static const ll Zp = 1000000009;
static const double EPS = 1e-9;

// 1 2 3 4
// 1 i j k
int mp[4][4] = {
    {1,  2,  3,  4},
    {2, -1,  4, -3},
    {3, -4, -1,  2},
    {4,  3, -2, -1}
};

int T;

map<vi, bool> DPj;
map<vi, bool> DPk;

bool chkk(vi ds, int c){
    vector<int> v(ds.begin()+c, ds.end());
    auto fi = DPk.find(v);
    if (fi != DPk.end()) {
        return fi->second;
    }
    int d = 1;
    rep(i,c,ds.size()) {
        d = mp[abs(d)-1][abs(ds[i])-1] * ((d>0)-(d<0)) * ((ds[i]>0)-(ds[i]<0));
    }
    if (d == 4) {
        DPk[v] = true;
        return true;
    }
    DPk[v] = false;
    return false;
}

bool chkj(vi ds, int c){
    vi v(ds.begin()+c, ds.end());
    auto fi = DPj.find(v);
    if (fi != DPj.end()) {
        return fi->second;
    }
    int d = 1;
    rep(i,c,ds.size()-1) {
        d = mp[abs(d)-1][abs(ds[i])-1] * ((d>0)-(d<0)) * ((ds[i]>0)-(ds[i]<0));
        if (d == 3) {
            if (chkk(ds, i+1)) {
                DPj[v] = true;
                return true;
            }
        }
    }
    DPj[v] = false;
    return false;
}

bool solve(vi ds){
    if (ds.size()<3) return false;

    int d = 1;
    rep(i,0,ds.size()-2) {
        d = mp[abs(d)-1][abs(ds[i])-1] * ((d>0)-(d<0)) * ((ds[i]>0)-(ds[i]<0));
        if (d == 2) {
            if (chkj(ds, i+1)) {
                return true;
            }
        }
    }
    return false;
}

int main(int argc, char *argv[]) {
    map<char, int> im;
    im['i'] = 2;
    im['j'] = 3;
    im['k'] = 4;

    cin>>T;
    for(int t=1;t<=T;++t) {
        DPj.clear();
        DPk.clear();
        int n, c;
        cin >> n >> c;
        vector<int> ds;
        string s;
        cin >> s;
        rep(i,0,c) {
            rep(j,0,n) {
                ds.pb(im[s[j]]);
            }
        }
        cout<<"Case #"<<t<<": "<<((solve(ds))?"YES":"NO")<<endl;
    }
    return 0;
}
