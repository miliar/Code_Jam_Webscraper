#include <iostream>
#include <cstdio>
#include <string>
#include <utility> // pair
#include <vector>
#include <algorithm>
#include <map>
#include <cstring> //memset
using namespace std;
  
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef long long ll;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define rep(i,n) for (i=0; i<n ; i++)
#define rep1(i,n) for (i=1; i<=n ; i++)
#define MOD 1000000007
#define MAX 111111
ll a[MAX];

int main () {

    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
    ll t, i, n, ff, ss, maxx = 0, z = 0;

    scanf("%lld", &t);
    while (t--) {
        scanf("%lld", &n);
        rep(i,n) {
            scanf ("%lld", &a[i]);
        }

        ff = maxx = 0;
        rep1(i, n-1) {
            if(a[i] - a[i-1] < 0){
                ff += (a[i-1] - a[i]);
            }
            maxx = max(maxx, (a[i-1]-a[i]));
        }
        ss = 0;
        rep(i, n-1) {
            if(a[i] >= maxx)
                ss += maxx;
            else ss += a[i];
        }
        printf("Case #%lld: %lld %lld\n",++z, ff, ss );
        // cout << "Case #" << ++z << ": " << ff << " " << ss << "\n";
    }
    return 0;
}