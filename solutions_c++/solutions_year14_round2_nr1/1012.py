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
#define VI V<int>
#define VII V<VI>
#define FOR(t,l,r) for (int t=l; t<(int)r; t++)
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
#define mii map<int,int>
#define pii pair<int,int>
#define x first
#define y second

#define Vpci V<pair<char,int> >
int bs (int x) {return (x<0)?-x:x; }

int main () {
	//freopen("input.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T; cin >>T;
	FOR(tt,1,T+1) {
		int n; cin >>n;
		V<string> s(n); FOR(t,0,n) cin >>s[t];
		V<Vpci> a;
		FOR(t,0,n) {
			Vpci d;
			int m=(int)s[t].sz;
			FOR(i,0,m)
				if (!d.empty() && d[(int)d.sz-1].x==s[t][i])
					d[(int)d.sz-1].y++;
				else
					d.pb(mp(s[t][i],1));
			a.pb(d);
		}
		int len=(int)a[0].sz, f=0;
		FOR(t,1,n)
			if ((int)a[t].sz!=len) {
				cout <<"Case #"<<tt<<": Fegla Won\n";
				f=1;
				break;
			}
		if (f) continue;
		int ans=0;
		FOR(i,0,len) {
			VI b(1,a[0][i].y);
			FOR(t,1,n) {
				if (a[t][i].x!=a[0][i].x) {
					f=1;
					break;
				}
				b.pb(a[t][i].y);
			}
			if (f) break;
			sort(all(b));
			int k=(int)b.sz, cur=(1<<30), temp=b[0];
			for (; temp<=b[k-1]; ++temp) {
				int sum=0;
				FOR(j,0,k) sum+=bs(b[j]-temp);
				cur=min(cur,sum);
			}
			ans+=cur;
		}
		if (f) cout <<"Case #"<<tt<<": Fegla Won\n";
		else cout <<"Case #"<<tt<<": "<<ans<<'\n';
	}
return 0;
}








