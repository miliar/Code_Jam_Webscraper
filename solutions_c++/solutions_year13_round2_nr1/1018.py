#include <algorithm>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <list>
#include <queue>
using namespace std;

#define LL long long
#define V vector
#define VD V<double>
#define VI V<LL>
#define VII V<VI>
#define FOR(t,l,r) for (LL t=l; t<(LL)r; t++)
#define FORL(t,l,r) for (LL t=l; t<(LL)r; t++)
#define max(x,y) ((x>y)?x:y)
#define min(x,y) ((x<y)?x:y)
#define abs(x) (((x)<0)?-(x):(x))
const double mth_pi=2*acos(0.);
#define pi mth_pi
#define inf (1<<23)
#define eps 1e-10
#define pb push_back
#define mp make_pair
#define sz size()
#define all(a) a.begin(),a.end()
#define mii map<LL,LL>
#define pii pair<LL,LL>
#define x first
#define y second

int main () {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	LL T; cin >>T;
	FOR(tt,1,T+1) {
		LL s, n, ans=0; cin >>s>>n;
		VI a(n); FOR(t,0,n) cin >>a[t];
		sort(all(a)); VI cur;
		if (s==1) {
			cout <<"Case #"<<tt<<": "<<n<<endl;
			continue;
		}
		FOR(t,0,n) {
			if (s>a[t]) {
				s+=a[t];
				continue;
			}
			cur.pb(ans+n-t);
			s=2*s-1, --t;
			ans++;
		}
		if (cur.sz) {
			sort(all(cur));
			if (ans>cur[0]) ans=cur[0];
		}
		cout <<"Case #"<<tt<<": "<<ans<<endl;
	}
return 0;
}
