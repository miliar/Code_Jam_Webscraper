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
ll SM;
vector<ll> SS;

ll solve(){
    ll c = 0;
    ll f = 0;
    for (int k=0; k<=SM; ++k) {
        if (SS[k] == 0) {
            continue;
        }
        f += max(0LL, k-c);
        c += SS[k] + max(0LL,k-c);
//        cout << k << ":" << f << "," << c << endl;
    }
    return f;
}

int main(int argc, char *argv[]) {
    cin>>T;
    for(int t=1;t<=T;++t) {
        SS.clear();
        string st;
        cin>>SM>>st;
        for (int k=0; k<=SM; ++k) {
            int s = st[k]-'0';
            SS.push_back(s);
        }
        cout<<"Case #"<<t<<": "<<solve()<<endl;
    }
    return 0;
}
