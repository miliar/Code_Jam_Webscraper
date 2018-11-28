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

vector<int> v;

int main() {
    int T;
    cin >> T;
    for(int TT = 0; TT < T; ++TT) {
        cout << "Case #" << TT + 1 << ": ";
        int n;
        cin >> n;
        v.clear();
        for(int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            v.pb(x);
        }
        int ans = 0;
        int l = 0, r = v.size() - 1;
        while(l != r) {
            int ind = l;
            for(int i = l; i <= r; ++i) {
                if (v[i] < v[ind]) ind = i;
            }
            if (ind - l < r - ind) {
                while(ind != l) {
                    swap(v[ind], v[ind - 1]);
                    --ind;
                    ++ans;
                }
                ++l;
            } else {
                while(ind != r) {
                    swap(v[ind], v[ind + 1]);
                    ++ind;
                    ++ans;
                }
                --r;
            }
        }
        cout << ans << endl;
    }
    return 0;
};
