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

LL gcd (LL a, LL b) {
	while (a%=b) swap(a,b);
return b;
}

bool chk (LL p, LL r, LL q) {
	//p*r>=q
	LL d=gcd(r,q); r/=d, q/=d;
	if (q==1ll) return 1;
	return (p>=q);
}

int main () {
	//freopen("input.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T; cin >>T;
	FOR(tt,1,T+1) {
		string s; cin >>s;
		LL p=0, q=0; bool f=0;
		FOR(i,0,s.sz) {
			if (s[i]=='/') {f=1; continue;}
			if (!f) p*=10, p+=(LL)(s[i]-'0');
			if (f) q*=10, q+=(LL)(s[i]-'0');
		}
		LL d=gcd(p,q); p/=d, q/=d;
		LL r=q; f=0;
		while (r) {
			if (r&1 && r>1) {
				cout <<"Case #"<<tt<<": impossible\n";
				f=1; break;
			}
			r>>=1ll;
		}
		if (f) continue;
		int ans=0; r=1;
		while (1) {
			if (chk(p,r,q)) break;
			ans++, r<<=1ll;
		}
		cout <<"Case #"<<tt<<": "<<ans<<'\n';
	}
return 0;
}








