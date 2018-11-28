#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:200000000")

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <utility>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <limits>
#include <cassert>
#include <ctime>
#include <list>
#include <bitset>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
 
template<typename T> inline T Abs(T a){ return a>0 ? a : -a; }
template<typename T> inline T sqr(T a){ return a*a; }
template<typename T> inline void relaxMin(T &a,T b){ if (b<a) a=b; }
template<typename T> inline void relaxMax(T &a,T b){ if (b>a) a=b; }

#define _(a,val) memset(a,val,sizeof a);
#define REP(i, a, b) for(int i(a),_bb(b); i < _bb; ++i)
//#define REP(i, a, b) for(int i = (a); i < (b); ++i)
#define REPD(i, a, b) for(int i = (b) - 1; i >= a; --i)
#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()
 
const int INF = (int)1E9;
//const int INF = INT_MAX/2-1;
const long double EPS = 1E-9;
const long double PI = 3.1415926535897932384626433832795;
#define y0 idfgosfgdgdfgd
#define y1 idfgoseincdjkg
typedef vector<int> vint;
typedef pair<int,int> pii;

#undef assert
#define assert(expr){if (!(expr)) { ++*(char*)0; } }

//#define MAXN (10*1000)
#define MAXN (10*1000*1000)
int ok[MAXN+1];
int ok2[MAXN+1];
int cnt[MAXN+1];

int digits[20];
int dcnt;

int ok0(ll v){
	dcnt = 0;
	while(v){
		digits[dcnt++]=v%10;
		v/=10;
	}
	REP(i,0,dcnt/2)
		if (digits[i] != digits[dcnt-1-i])
			return 0;
	return 1;
}

ll root_gr(ll v){
	ll ans = (ll)sqrt(v+.0);
	for(int d=-2;d<=2;d++)
		if (sqr(ans+d)>=v)
			return ans+d;
	assert(false);
	return 0;
}
ll root_ls(ll v){
	ll ans = (ll)sqrt(v+.0);
	for(int d=2;d>=-2;d--)
		if (sqr(ans+d)<=v)
			return ans+d;
	assert(false);
	return 0;
}

void solve(){
	ll a,b; cin>>a>>b;
	ll ra=root_gr(a),rb=root_ls(b);
	if (ra > rb) cout<<0<<endl;
	else cout<<cnt[rb]-cnt[ra-1]<<endl;
}

void pre(){
	for(int i=1;i<=MAXN;i++)
		ok[i]=ok0(i);
	for(int i=1;i<=MAXN;i++)
		if (ok[i])
			ok2[i]=ok0(i*1LL*i);
	for(int i=1;i<=MAXN;i++)
		cnt[i]=cnt[i-1]+ok2[i];
}

int main(){
#ifdef acm
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	freopen("error.txt", "wt", stderr);
#endif
	srand(time(0));
	//srand(0xA1B2C3D4);

	pre();

	int t; cin>>t;
	REP(i,0,t){
		printf("Case #%d: ",i+1);
		solve();
	}

#ifdef acm
	printf("\n\n\n\n\n%.3lf\n", clock()*1e-3);
#endif
	return 0;
}