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



int main(void){
	int T;
	cin >> T;
	rep(testcase,1,T+1){
		cerr << testcase << endl;
		int n;
		cin >> n;

		int ans=1010;

		int mask=0;
		rep(i,n)rep(j,n){
			char in;
			cin >> in;
			mask|=( (in=='1') <<(n*i+j));
		}

		const int m=4*n;
		rep(mask2,1<<m){
			if((mask&mask2)!=0) continue;
			int cur=__builtin_popcount(mask2);
			const int nmask=mask|mask2;

			bool ok=true;
			int order[4]={0,1,2,3};

			do{
				bool can[5][16];
				rep(i,5)rep(j,16) can[i][j]=false;
				can[0][0]=true;

				rep(i,n)rep(mask3,1<<n){
					if(can[i][mask3]==false) continue;

					bool found=false;
					rep(k,n){
						if(mask3&(1<<k)) continue;
						if((nmask&(1<<(n*order[i]+k)))==0) continue;
						can[i+1][mask3|(1<<k)]=true;
						found=true;
					}
					if(found==false) ok=false;
				}

			}while(next_permutation(order,order+n));

			if(ok) chmin(ans,cur);
		}

		cout  << "Case #" << testcase << ": " << ans << endl;
	}
	return 0;
}