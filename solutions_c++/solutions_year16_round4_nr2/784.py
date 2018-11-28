#include <bits/stdc++.h>

#define _overload(_1,_2,_3,name,...) name
#define _rep(i,n) _range(i,0,n)
#define _range(i,a,b) for(int i=int(a);i<int(b);++i)
#define rep(...) _overload(__VA_ARGS__,_range,_rep,)(__VA_ARGS__)

#define _rrep(i,n) _rrange(i,n,0)
#define _rrange(i,a,b) for(int i=int(a)-1;i>=int(b);--i)
#define rrep(...) _overload(__VA_ARGS__,_rrange,_rrep,)(__VA_ARGS__)

#define _all(arg) begin(arg),end(arg)
#define uniq(arg) sort(_all(arg)),(arg).erase(unique(_all(arg)),end(arg))
#define getidx(ary,key) lower_bound(_all(ary),key)-begin(ary)
#define clr(a,b) memset((a),(b),sizeof(a))
#define bit(n) (1LL<<(n))
#define popcount(n) (__builtin_popcountll(n))

template<class T>bool chmax(T &a, const T &b) { return (a<b)?(a=b,1):0;}
template<class T>bool chmin(T &a, const T &b) { return (b<a)?(a=b,1):0;}

using namespace std;
using ll=long long;

using R=long double;

R dp[210][210];
vector<R> ary;

R calc(){
	int n=ary.size();
	rep(i,210)rep(j,210) dp[i][j]=0.0;
	dp[0][0]=1.0;

	rep(i,n)rep(j,n){
		dp[i+1][j+1]+=dp[i][j]*ary[i];
		dp[i+1][j]+=dp[i][j]*(1.0-ary[i]);
	}

	return dp[n][n/2];
}


int main(void){
	int T;
	cin >> T;
	rep(testcase,1,T+1){
		cerr << testcase << endl;
		int n,k;
		cin >> n >> k;

		R ans=0.0;

		vector<R> pro;
		rep(i,n){
			R in;
			cin >> in;
			pro.push_back(in);
		}

		rep(mask,1<<n){
			ary.clear();
			if(__builtin_popcount(mask)!=k) continue;
			rep(i,n) if(mask&(1<<i)) ary.push_back(pro[i]);
			chmax(ans,calc());
		}
		
		cout.precision(20);
		cout << fixed << "Case #" << testcase << ": " << ans << endl;
	}
	return 0;
}