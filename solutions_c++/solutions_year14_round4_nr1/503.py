#pragma comment(linker, "/STACK:65000000")
#include <algorithm>
#include <cmath>
#include <cstdio> 
#include <cstring> 
#include <iostream> 
#include <map> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <string> 
#include <vector> 

using namespace std; 

template<class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

typedef long long lng;
typedef long double ld;
typedef stringstream istr;

#define TynKogep TOPCODER
#define bublic public:
#define pb push_back
#define sz(x) ((int)(x).size())
#define mp make_pair
#define first fi
#define second se
#define clr(a) memset((a),0,sizeof(a))

int T;
vector<int> v;

int main() {
    int T;
    cin >> T;
    for(int TT = 0; TT < T; ++TT) {
        cout << "Case #" << TT + 1 << ": ";
        int n, x;
        cin >> n >> x;
        for(int i = 0; i < n; ++i) {
            int z;
            cin >> z;
            v.pb(z);
        }
        sort(v.begin(), v.end());
        int ans = 0;
        for(int i = v.size() - 1; i >= 0; --i) {
            if (!v[i]) continue;
            for(int j = i - 1; j >= 0; --j) {
                if (!v[j]) continue;
                if (v[i] + v[j] <= x) {
                    ++ans;
                    v[i] = 0;
                    v[j] = 0;
                    break;
                }
            }
            if (v[i]) {
                ++ans;
                v[i] = 0;
            }
        }
        cout << ans << endl;
    }
    return 0;
};
