#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdarg>
#include <cassert>
#include <climits>
#include <cstring>
#include <complex>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pi;
typedef vector<int> vi;


#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define x first
#define y second
#define y1 y1_gdssdfjsdgf
#define y0 y0_fsdjfsdogfs
#define ws ws_fdfsdfsdgfs
#define image(a) {sort(all(a)),a.resize(unique(all(a))-a.begin());}
#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}

#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )
#define problem_name "a"
int n, m;
string s[10000];
string cur[10000];
int res1, res2;
int lcp(string a, string b) {
    int ans = 0;
    while (ans < sz(a) && ans < sz(b)) {
        if (a[ans] == b[ans]) {
            ans++;
        } else {
            break;
        }
    }
    ans = sz(b) - ans;
    if (sz(a) == 0) {
        ans++;
    }
    return ans;
}
void bct(int k, int curs) {
    if (k == n) {
        if (curs > res1) {
            res1 = curs;
            res2 = 1;
        } else
        if (curs == res1) {
            res2++;
        }
        return;        
    }
    for (int i = 0; i < m; i++) {
        string old = cur[i];
        cur[i] = s[k];
        bct(k + 1, curs + lcp(old, cur[i]));
        cur[i] = old;
    }
}
int main(){
    #ifdef home
    assert(freopen(problem_name".out","wt",stdout));
    assert(freopen(problem_name".in","rt",stdin));
    #endif
    int T;
    cin>>T;
    for (int ti = 1; ti <= T; ti++) {
        printf("Case #%d: ", ti);
        cin>>n>>m;
        for (int i = 0; i < n; i++) {
            cin>>s[i];
        }
        sort(s, s + n);
        for (int i = 0; i < m; i++) {
            cur[i] = "";
        }
        res1 = 0;
        res2 = 0;
        bct(0, 0);
        printf("%d %d\n", res1, res2);
    }
    return 0;
}
