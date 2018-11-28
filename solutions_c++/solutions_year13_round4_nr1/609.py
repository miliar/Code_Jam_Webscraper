#define _CRT_SECURE_NO_DEPRECATE
//#pragma comment(linker, "/STACK:200000000")

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

#ifdef NDEBUG
#undef assert
#define assert(expr){if (!(expr)) { ++*(char*)0; } }
//#define assert(expr){if (!(expr)) { char *a=0; *a=10; } }
#endif


void pre(){
	//
}

struct ev{
	int id;
	int time;
	bool open;
	ev(){}
	ev(int id,int time,bool open) : id(id),time(time),open(open){}
	bool operator<(const ev&o)const{
		if (time != o.time)
			return time < o.time;
		return open > o.open;
	}
};
vector<int> sall;
vector<int> eall;
vector<int> cntall;

vector<pii> cur;

ll f(ll n){
	return n*(n-1)/2;
}

void solve(){
	sall.clear();
	eall.clear();
	cntall.clear();
	vector<ev> vev;
	int n,m; cin>>n>>m;
	REP(i,0,m){
		int s,e,cnt; cin>>s>>e>>cnt;
		vev.push_back(ev(i,s,true));
		vev.push_back(ev(i,e,false));
		sall.push_back(s);
		eall.push_back(e);
		cntall.push_back(cnt);
	}
	sort(all(vev));
	cur.clear();
	ll ans = 0;
	REP(i,0,2*m){
		ev e = vev[i];
		if (e.open){
			cur.push_back(mp(e.id,cntall[e.id]));
		}else{
			int need_cnt = cntall[e.id];
			while(need_cnt>0 && !cur.empty()){
				int id = cur.back().first;
				int cnt = cur.back().second;
				cur.pop_back();

				int gcnt = min(need_cnt,cnt);
				ll payed = f(e.time-sall[id])*1LL*gcnt;
				ll npayed = f(eall[id]-sall[id])*1LL*gcnt;
				ans+=payed-npayed;

				need_cnt-=gcnt;
				cnt-=gcnt;

				if (cnt>0)
					cur.push_back(mp(id,cnt));
			}
		}
	}
	cout<<ans<<endl;
}


//#define TASK "equality"
int main(){
#ifdef acm
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	//freopen("error.txt", "wt", stderr);
#else
	//freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);
	//freopen(TASK".in", "rt", stdin);
	//freopen(TASK".out", "wt", stdout);
#endif
	srand(0xA1B2C3D4);

	pre();
	int tc; cin>>tc;
	for(int i=1;i<=tc;i++){
		printf("Case #%d: ",i);
		solve();
	}


#ifdef acm
	//printf("\n\n\n\n\n%.3lf\n", clock()*1e-3);
#endif
	return 0;
}