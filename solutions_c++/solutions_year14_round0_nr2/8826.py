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

int gcd (int a, int b) {
	while (a%=b) swap(a,b);
return b;
}

int main () {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cout.precision(7);
	cout.setf(ios::fixed);
	int T; cin >>T;
	FOR(tt,1,T+1) {
		long double c, f, x; cin >>c>>f>>x;
		long double y=x/c;
		long double cur=0., ans=x, s=2.;
		while (cur<ans) {
			if (cur+y/s<ans) ans=cur+y/s;
			cur+=1/s, s+=f;
		}
		cout <<"Case #"<<tt<<": "<<c*ans<<endl;
	}
return 0;
}







