#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:200000000")

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <functional>
#include <numeric>
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
#include <complex>
//#include <tuple>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
 
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
const long double EPS = 1E-6;
const long double PI = 3.1415926535897932384626433832795;
#define y1 idfgoseincdjkg
typedef vector<int> vint;
typedef pair<int,int> pii;

#undef assert
#define assert(expr){if (!(expr)) { ++*(char*)0; } }

int n;
int a[1000];
int aa[1000];
int b[1000];
int x[1000];
int perm[1000];

int brute(){
	map<int,int> pos;
	REP(i,0,n) pos[a[i]]=i;

	REP(i,0,n) x[i]=a[i];
	sort(x,x+n);

	int ans = n*n;
	do{
		bool ok = true;
		int mi = max_element(x,x+n)-x;
		REP(i,0,n){
			if (i < mi) ok &= x[i] < x[i+1];
			if (i > mi) ok &= x[i-1] > x[i];
		}
		if (!ok) continue;
		REP(i,0,n) perm[i]=pos[x[i]];
		int v = 0;
		REP(i,0,n) REP(j,0,n) if (i < j && perm[i] > perm[j]) v++;
		ans=min(ans,v);
	}while(next_permutation(x,x+n));
	return ans;
}

void solve(){
	cin>>n;
	REP(i,0,n) cin>>a[i];

	int p = 0;
	REP(i,0,n) if (a[i] > a[p]) p = i;

	int ans = n*n*10+100;

	for(int i=0,j=0;i<n;i++) if (i!=p) aa[j++]=a[i];

	map<int,int> val2pos;
	REP(i,0,n) val2pos[a[i]]=i;

	REP(pos,0,n){
		REP(i,0,n) b[i]=aa[i];
		REPD(i,pos+1,n) b[i]=b[i-1];
		b[pos]=a[p];

		sort(b,b+pos,less<int>());
		sort(b+pos,b+n,greater<int>());

		REP(i,0,n) perm[i]=val2pos[b[i]];
		//REP(i,0,n) cout<<x[i]<<" "; cout<<endl;

		int d = 0;

		REP(i,0,n) REP(j,0,n) if (perm[i] > perm[j] && i < j) d++;

		//int d = abs(pos-p);
		//REP(i,0,pos) REP(j,0,pos) if (aa[i] > aa[j] && i < j) d++;
		//REP(i,pos,n-1) REP(j,pos,n-1) if (aa[i] < aa[j] && i < j) d++;

		ans=min(ans,d);
		d=d;
	}
	int ans2 = brute();
	//assert(ans==ans2);
	//cout<<ans<<endl;
	cout<<ans2<<endl;
}



#define TASK ""
int main(){
	//freopen("input.txt", "wt", stdout);
	//freopen("input.txt", "wt", stdin);
#ifdef acm
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	freopen("error.txt", "wt", stderr);
#else
	//freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);
	//freopen(TASK".in", "rt", stdin);
	//freopen(TASK".out", "wt", stdout);
#endif
	//srand(time(0));
	//srand(0xA1B2C3D4);

	//pre();
	int tc; scanf("%d\n",&tc);
	for(int t=1;t<=tc;t++){
		printf("Case #%d: ",t);
		solve();
	}
	//solve();


#ifdef acm
	//printf("\n\n\n\n\n%.3lf\n", clock()*1e-3);
#endif
	return 0;
}