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

#define FOR(t,l,r) for (int t=l; t<r; t++)
#define min(x,y) ( ((x)<(y))?(x):(y) )
#define max(x,y) ( ((x)>(y))?(x):(y) )
#define abs(x) (((x)<0)?-(x):(x))
#define sgn(x) ((x)>0)-((x)<0)
const double math_pi=2*acos(0.);
#define pi math_pi
#define inf (1<<23)
#define eps 1e-7
#define pb push_back
#define mp make_pair
#define sz size()
#define LL long long
#define V vector
#define VI V<int>
#define VII V<VI>
#define all(a) a.begin(),a.end()
#define mii map<int,int>
#define pii pair<int,int>
#define x first
#define y second

LL pals[39]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

int main () {
	freopen("C-large-1.in","r",stdin);
	freopen("C-large-1.out","w",stdout);
	int T; cin >>T;
	FOR(tt,1,T+1) {
		LL a, b; cin >>a>>b;
		int ans=0;
		FOR(t,0,39)
			ans+=(pals[t]>=a && pals[t]<=b);
		cout <<"Case #"<<tt<<": "<<ans<<endl;
	}
return 0;
}
