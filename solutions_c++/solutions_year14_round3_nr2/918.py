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

static const ll Zp = 1000000007;

int T;
int N;

ll check(const vector<int> &idx, vector<string> &ts)
{
    string m;
    rep(i,0,N) {
        m += ts[idx[i]];
    }

    int l = m.size();
    char c=m[0];
    rep(i,1,l) {
        if (m[i] == c) continue;
        if (m.find(c, i) != string::npos) return 0;
        c = m[i];
    }

//    cout << m << endl;
    return 1;
}

int main(int argc, char *argv[]) {
    cin>>T;
    for(int t=1;t<=T;++t) {
        vector<string> ts;
        vector<int> idx;
        cin>>N;
        rep(i,0,N) {
            string s;
            cin>>s;
            ts.pb(s);
            idx.pb(i);
        }
        ll ans = 0;
        do {
            ans += check(idx, ts);
            ans = ans % Zp;
        } while (next_permutation(idx.begin(), idx.end()));

        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
