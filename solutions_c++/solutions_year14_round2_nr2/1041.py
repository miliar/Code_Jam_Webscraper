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

int main () {
	//freopen("input.txt","r",stdin);
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T; cin >>T;
	FOR(tt,1,T+1) {
		int A, B, K; cin >>A>>B>>K;
		int ans=0;
		FOR(a,0,A) FOR(b,0,B)
			if ((a&b)<K) ans++;
		cout <<"Case #"<<tt<<": "<<ans<<'\n';
	}
return 0;
}








