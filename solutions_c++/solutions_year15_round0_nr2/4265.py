// =====================================================================================
//       Filename:  panCake.cpp
//    Description:  
//        Created:  04/11/2015 08:25:08 PM
//         Author:  BrOkEN@!
// =====================================================================================

#include<fstream>
#include<iostream>
#include<sstream>
#include<bitset>
#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#include<iterator>
#include<string>
#include<cassert>
#include<cctype>
#include<climits>
#include<cmath>
#include<cstddef>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>

#define INF (1<<30)
#define EPS 1e-9

using namespace std;

template< class T > inline T maxxyz(T x,T y,T z) {return max(max(x,y),z);}
template< class T > inline T minxyz(T x,T y,T z) {return min(min(x,y),z);}
template< class T > inline T abs(T n) { return (n < 0 ? -n : n); }
template< class T > inline T sqrt(T x) { return x * x; }
template< class T > inline T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > inline T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > inline bool in_range(T x, T i, T y) { return x<=i && i<=y; }
template< class T > inline int comp(T x, T y) { return ((x+EPS < y) ? -1 : ((x > y+EPS)?1:0)); }
template< class T > inline bool gt(T x, T y) { return (comp(x,y)==1); }
template< class T > inline bool lt(T x, T y) { return (comp(x,y)==-1); }
template< class T > inline bool eq(T x, T y) { return (comp(x,y)==0); }

#define typeof __typeof
#define FOR(i,a,b) for(typeof((a)) i=(a); i <= (b) ; ++i)
#define REV_FOR(i,a,b) for(typeof((a)) i=(a); i >= (b) ; --i)
#define FOREACH(it,x) for(typeof((x).begin()) it=(x).begin(); it != (x).end() ; ++it)
#define REV_FOREACH(it,x) for(typeof((x).rbegin()) it=(x).rbegin(); it != (x).rend() ; ++it)
#define ALL(x) (x).begin(),(x).end()
#define SIZE(x) ((int)((x).size()))
#define SET(p, v) memset(p, v, sizeof(p))
#define CLR(p) SET(p,0)
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define ARRAY_SIZE(array) (sizeof(array) / sizeof((array)[0]))
#define PB push_back
#define MP make_pair

typedef long long __int64;
typedef unsigned long long __uint64;
typedef pair<int,int> II;
typedef vector<int> VI;
typedef vector<II> VII;
typedef map<int,int>	MII;
typedef map<string,int>	MSI;

const int MAX= 1010;

int P[MAX],D;

int solve(){
	int ans = P[0];
	FOR(i,1,P[0]){
		int now = 0, nmax = 0;

		FOR(j,1,D){
			if(P[j]>i){
				now += (P[j]/i) + (((P[j]%i==0)?0:1) - 1);
				nmax = max(nmax,i);
			}else{
				nmax = max(nmax,P[j]);
			}

		}

		now += nmax;
		ans = min(ans,now);
	}

	return ans;
}

int main(){
	ios_base::sync_with_stdio(0);
	int T=0;
	scanf("%d",&T);
	FOR(t,1,T){
		CLR(P);
		scanf("%d",&D);
		FOR(i,1,D){
			scanf("%d",&P[i]);
			P[0]=max(P[0],P[i]);
		}
		printf("Case #%d: %d\n",t,solve());
	}
	return 0;
}

