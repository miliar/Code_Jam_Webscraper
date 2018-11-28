#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <numeric>
#include <memory.h>
#include <cstdio>
#include <assert.h>

using namespace std;

#define pb push_back
#define INF 1011111111
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define rep(i,n) FOR(i,0,n)
#define CL(a,v) memset((a),(v),sizeof(a))
#define mp make_pair
#define X first
#define Y second
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> pii;

/*** TEMPLATE CODE ENDS HERE */

int s[10000];
bool was[10000];

int main() {
#ifdef LOCAL_HOST
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    ios_base::sync_with_stdio(false);
    
    int T;
    cin >> T;
    
    FOR(cs,1,T+1) {
        int n, x;
        cin >> n >> x;
        rep(i,n) cin >> s[i];
        sort(s,s+n);
        fill(was,was+n,false);
        int ans = 0;
        for(int i = n-1, j=n-2;;--i) {
            while(i>=0 && was[i]==true) --i;
            if(i<0) break;
            was[i] = true;
            ++ans;
            if(i>=j) j=i-1;
            while(j>=0 && (was[j]==true || s[j]+s[i] > x)) --j;
            if(j>=0) {
                was[j] = true;
                --j;
            }
        }
        
        cout << "Case #" << cs << ": " << ans << endl;
    }
    
    return 0;
}
