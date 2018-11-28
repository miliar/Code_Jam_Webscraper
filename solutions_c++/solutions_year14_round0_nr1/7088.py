#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
 
using namespace std;
 
#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)
#define INF						(int)1e9
#define LINF					(long long)1e18
#define EPS						1e-9
#define maX(a,b)				((a)>(b)?(a):(b))
#define miN(a,b)				((a)<(b)?(a):(b))
#define abS(x)					((x)<0?-(x):(x))
#define FOR(i,a,b)				for(int i=a;i<b;i++)
#define REP(i,n)				FOR(i,0,n)
#define foreach(v,c)			for(typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define mp						make_pair
#define FF						first
#define SS						second
#define tri(a,b,c)				mp(a,mp(b,c))
#define XX						first
#define YY						second.first
#define ZZ						second.second
#define pb						push_back
#define fill(a,v) 				memset(a,v,sizeof a)
#define all(x)					x.begin(),x.end()
#define SZ(v)					((int)(v.size()))
#define DREP(a)					sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)			(lower_bound(all(arr),ind)-arr.begin())
#define debug(args...)			{dbg,args; cerr<<endl;}
#define dline					cerr<<endl
 
void sc(char &c){
	char temp[4];
	ss(temp);
	c=temp[0];
}
 
struct debugger{
	template<typename T> debugger& operator , (const T& v){	
		cerr<<v<<" ";
		return *this;
	}
} dbg;
 
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<int,PII> TRI;
 
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<PII> VII;
typedef vector<PLL> VLL;
typedef vector<TRI> VT;
 
typedef vector<VI> VVI;
typedef vector<VL> VVL;
typedef vector<VII> VVII;
typedef vector<VLL> VVLL;
typedef vector<VT> VVT;
 
//Main Code Starts
 
int main(){

	int tc;
	int ans1, ans2;
	int cards1[4][4], cards2[4][4];
	VI possible1, possible2;

	s(tc);

	FOR(i, 1, tc+1){

		possible1.clear();
		possible2.clear();

		// First set of input

		s(ans1);

		REP(i, 4)
			REP(j, 4)
				s(cards1[i][j]);

		REP(i, 4)
			possible1.pb(cards1[ans1-1][i]);

		// Second set of input

		s(ans2);

		REP(i, 4)
			REP(j, 4)
				s(cards2[i][j]);

		REP(i, 4)
			possible2.pb(cards2[ans2-1][i]);

		// Compute

		int match = 0, match_no;

		foreach(v1, possible1){
			foreach(v2, possible2){
				if(*v1 == *v2){
					match++;
					match_no = *v1;
				}
			}
		}

		if(match == 1){
			printf("Case #%d: %d\n", i, match_no);
		} else if(match > 1){
			printf("Case #%d: Bad magician!\n", i);
		} else if(match == 0){
			printf("Case #%d: Volunteer cheated!\n", i);
		}
	}

	return 0;
}























