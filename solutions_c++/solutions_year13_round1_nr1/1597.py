#include <iostream>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <stack>
#include <utility>
#include <numeric>
#include <algorithm>
#include <functional>
#include <cctype>
#include <complex>
#include <string>
#include <sstream>

using namespace std;

#define all(c) c.begin(),c.end()
#define rall(c) c.rbegin(),c.rend()
#define rep(i,n) for(int i=0;i<(n);i++)
#define tr(it,container) for(typeof(container.begin()) it = container.begin(); \
                                                  it != container.end(); ++it)
#define mp(a,b) make_pair((a),(b))
#define eq ==

typedef long long ll;
typedef complex<double> point;
typedef pair<int,int> pii;

// →↑←↓
const int dx[] = {1,0,-1,0};
const int dy[] = {0,-1,0,1};


const double EPS = 1e-9;

int main(){
    int T;
    cin >> T;
    for(int test_case=1;test_case<=T;test_case++){
        ll r,t,ans;
        cin >> r >> t;
        for(ll n=1;;n++){
            ll now = n * (2*r+2*n-1);
            if(now > t){
                ans = n-1;
                break;
            }
        }
        //Case #1: 1
        cout << "Case #" << test_case << ": " << ans << endl;
        //cout << ans << endl;
    }
    return 0;
}
