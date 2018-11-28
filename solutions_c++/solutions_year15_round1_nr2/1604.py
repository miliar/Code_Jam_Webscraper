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
int B;
ll N;
ll Bs[5];
ll Ms[5];

int solve(){
    ll minb = 0;

    ll lcm = 1;
    rep (i,0,B) {
        lcm = (lcm * Ms[i]) / gcd(lcm, Ms[i]);
        Bs[i] = 0;
    }
    ll ol = 0;
    rep (i,0,B) {
        ol += lcm / Ms[i];
    }

    ll rn = N % ol;
    minb = B-1;

    if (rn==0) { rn = ol; }

    for (ll i=0; i<rn; ++i) {
        minb = 0;
        ll minm = 999;
        rep(j,0,B) {
            if (Bs[j]< minm) {
                minm = Bs[j]; minb = j;
            }
        }
        rep(j,0,B) {
            Bs[j] -= minm;
        }
        Bs[minb] = Ms[minb];
    }
    return minb + 1;
}

int main(int argc, char *argv[]) {
    cin>>T;
    for(int t=1;t<=T;++t) {
        cin >> B >> N;
        rep(i,0,B) {
            Bs[i] = 0;
            cin >> Ms[i];
        }
        cout<<"Case #"<<t<<": "<<solve()<<endl;
    }
    return 0;
}
