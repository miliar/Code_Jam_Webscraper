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


bool cmp(const pair<int,string> &a,const pair<int,string> &b){
	if (a.second != b.second)
		return a.second < b.second;
	return a.first < b.first;
}

void pre(){
}

bool cmp2(pii a, pii b){
	if (a.second != b.second)
		return a.second < b.second;
	return a.first < b.first;
}

int rev(int v,int n){
	int ans = 0;
	REP(i,0,n) if (v&(1<<i)) ans|=1<<(n-i-1);
	return ans;
}

int N;
ll P;

void solve(){
	//int N,P; cin>>N>>P;
	if (P==1LL<<N){
		cout<<P-1<<" "<<P-1<<endl;
		return;
	}
	/*vector<pair<int,int>> users;
	REP(i,0,1<<N){
		users.push_back(mp(i,0));
	}
	REP(i,0,N){
		REP(j,0,(1<<N)/2){
			vector<pair<int,int>> &tmp = users;
			int a = 2*j;
			int b = 2*j+1;
			if (tmp[a].first < tmp[b].first){
				//a win

				//tmp[a].second+=1<<i;
				tmp[b].second+=1<<(N-i);
			}else{
				//b win

				//tmp[b].second+=1<<i;
				tmp[a].second+=1<<(N-i);
			}
		}
		sort(all(users),cmp2);
	}
	//REP(i,0,1<<N) cout<<users[i].first<<" "; cout<<endl;
	//REP(i,0,1<<N) cout<<rev(i,N)<<" "; cout<<endl;

	int ans_min = 0;
	REP(i,0,P){
		int id = users[i].first;
		ans_min=max(ans_min,id);
	}
	int ans_max = (1<<N)-1;
	REP(i,P,1<<N){
		int id = users[i].first;
		ans_max=min(ans_max,id);
	}
	if (P != 1<<N) ans_max--;
	
	cout<<ans_max<<" "<<ans_min<<endl;*/
	
	ll ans1 = 0;
	REP(i,0,N){
		if ((P-1)&(1LL<<(N-i-1))){
			ans1+=1LL<<(i+1);
		}else break;
	}
	ll ans2 = 0;
	REP(i,1,N+1){
		if ((P-1)>=(1LL<<(i))-1){
			ans2+=1LL<<(N-i);
		}
	}
	cout<<ans1<<" "<<ans2<<endl;
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
		cin>>N>>P;
		solve();
	}
	/*N=5;
	for(P=1;P<(1<<N);P++){
		cout<<P-1<<": ";
		solve();
	}*/


#ifdef acm
	//printf("\n\n\n\n\n%.3lf\n", clock()*1e-3);
#endif
	return 0;
}