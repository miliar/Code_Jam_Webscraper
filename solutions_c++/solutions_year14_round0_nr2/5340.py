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
#include <iomanip>

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

int T;

int main(int argc, char *argv[]) {
    cin>>T;
    for(int t=1;t<=T;++t) {
        double C, F, X;
        cin >> C >> F >> X;
        double nd = (X-C)/C - (2.0/F);
        ll n = ceil(nd);
        double te = X/2.0;
        double tt = 0.0;
        double A=2.0;
//        cout << "DBG:" << n << endl;
        for (ll i=0; i<n; ++i) {
            tt = tt + C/A;
            A += F;
            te = tt+X/A;
        };

        cout<<"Case #"<<t<<": "<<fixed<<setprecision(7)<<te<<endl;
    }
	return 0;
}
