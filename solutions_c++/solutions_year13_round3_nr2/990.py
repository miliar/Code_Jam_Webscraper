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
#define FOR(t,l,r) for (LL t=l; t<(int)r; t++)
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

int main () {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	LL T; cin >>T;
	FOR(tt,1,T+1) {
		int x0, y0; cin >>x0>>y0;
		string s="";
		if (x0<0) FOR(t,0,-x0) s+="EW";
		else FOR(t,0,x0) s+="WE";
		if (y0<0) FOR(t,0,-y0) s+="NS";
		else FOR(t,0,y0) s+="SN";
		cout <<"Case #"<<tt<<": "<<s<<endl;
	}
return 0;
}
