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
int N;
vector<ll> m;
ll s1;
ll s2;

void solve(){
    s1 = s2 = 0LL;
    ll diff = 0;

    rep(i,0,N-1) {
        diff = max(diff, m[i]-m[i+1]);
        s1 += max(0LL, m[i]-m[i+1]);
    }
    rep(i,0,N-1) {
        s2 += min(m[i], diff);
    }

    return;
}

int main(int argc, char *argv[]) {
    cin>>T;
    for(int t=1;t<=T;++t) {
        m.clear();
        cin >> N;
        rep(i,0,N) {
            int mi;
            cin >> mi;
            m.pb(mi);
        }

        solve();
        cout<<"Case #"<<t<<": "<<s1<<" "<<s2<<endl;
    }
    return 0;
}
