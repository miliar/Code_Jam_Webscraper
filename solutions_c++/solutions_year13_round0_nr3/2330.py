#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<string>
 
using namespace std;
 
#define s(n)                                 scanf("%d",&n)
#define sl(n)                                   scanf("%lld",&n)
#define sf(n)                                   scanf("%lf",&n)

#define EPS                                             1e-9
 
#define FOR(i,a,b)                              for(int i=a;i<b;i++)
#define REP(i,n)                                FOR(i,0,n)
#define foreach(v,c)            for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
 
#define mp                                              make_pair
#define pb                                              push_back
 
#define FF                                              first
#define SS                                              second
 
#define tri(a,b,c)                              mp(a,mp(b,c))
#define XX                                              first
#define YY                                              second.first
#define ZZ                                              second.second
 
/*Important ones*/
#define fill(a,v)                               memset(a,v,sizeof a)     //Works properly only for v = 0 or -1
#define all(x)                                  x.begin(),x.end()
 
#define SZ(v)                                   ((int)(v.size()))
#define DREP(a)                                 sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)                  (lower_bound(all(arr),ind)-arr.begin())
 
//typedefs. Use if you feel comfortable
typedef pair<int,int> PII;
typedef pair<long long,long long> PLL;
typedef pair< long long, PLL > TRI;

typedef vector<int> VI;
typedef long long LL;
typedef vector<LL> VL;
typedef vector<PII> VII;
typedef vector<PLL> VLL;
typedef vector<TRI> VT;
 
typedef vector<VI> VVI;
typedef vector<VL> VVL;
typedef vector<VII> VVII;
typedef vector<VLL> VVLL;
typedef vector<VT> VVT;

#define MAX 10010

LL tests, tp, A, B;
VL ans;

LL make1(int x){
	VI dig, rev;
	LL ret = 0;
	while(x){
		dig.pb(x%10);
		rev.pb(x%10);
		x /= 10;
	}
	reverse(all(rev));
	FOR(i,0,SZ(rev))
		ret = ret*10+rev[i];
	FOR(i,0,SZ(dig))
		ret = ret*10+dig[i];
	return ret;
}

LL make2(LL x){
	VI dig, rev;
	LL ret = 0;
	while(x){
		dig.pb(x%10);
		rev.pb(x%10);
		x /= 10;
	}
	reverse(all(rev));
	FOR(i,0,SZ(rev))
		ret = ret*10+rev[i];
	FOR(i,1,SZ(dig))
		ret = ret*10+dig[i];
	return ret;
}

bool check(LL x){
	VI dig, rev;
	while(x){
		dig.pb(x%10);
		rev.pb(x%10);
		x /= 10;
	}
	reverse(all(rev));
	FOR(i,0,SZ(dig)/2)
		if(dig[i] != rev[i])
			return 0;
	return 1;
}

int main(){
	
	sl(tests);
	FOR(i,1,MAX){
		tp = make1(i);
		if(check(tp*tp))
			ans.pb(tp*tp);
		tp = make2(i);
		if(check(tp*tp))
			ans.pb(tp*tp);
	}
	DREP(ans);
	FOR(testcase,0,tests){
		cin>>A>>B;
		cout<<"Case #"<<testcase+1<<": "<<upper_bound(all(ans), B)-lower_bound(all(ans), A)<<endl;
	}
	
	return 0;
	
}
