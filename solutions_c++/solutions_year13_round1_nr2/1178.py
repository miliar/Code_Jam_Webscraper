#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cassert>
#include<vector>
#include<string>
#include<iomanip>
#include<cstring>
#include<sstream>
#include<bitset>
#include<cstdio>
#include<cmath>
#include<climits>
#include<ctime>
#include<string>
#include<fstream>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#define ip(x) scanf("%d",&x)
#define ipLL(x) scanf("%lld",&x)
#define ForInc(var,beg,end) for(int var=beg;var<=end;++var)
#define advForInc(var,beg,end,inc) for(int var=beg;var<=end;var+=inc)
#define ForDec(var,end,beg) for(int var=end;var>=beg;--var)
#define ipArray(arr,size) ForInc(i,0,size-1) ip(arr[i]);
#define print(x) printf("%d\n",x)
#define printLL(x) printf("%lld\n",x)
#define ss(str) scanf("%s",str)
#define ii pair<int,int>
#define mp make_pair
#define pb push_back
#include<ctime>
template<typename T> T gcd(T a, T b) { return (b == 0) ? abs(a) : gcd(b, a % b); }
template<typename T> inline T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<typename T> inline T mod(T a, T b) { return (a % b + b) % b; }
template<typename T> inline T sqr(T x) { return x * x; }
typedef long long LL;
using namespace std;

/* Main Code starts here :) */
int E,R,N;
int v[20];
LL dp[20][20];
LL max(LL a, LL b){
	return (a>b)?a:b;
}
LL solve(int ix, int El){
	if(dp[ix][El]!=-1)return dp[ix][El];
	if(ix==N-1){
		return dp[ix][El]=(LL)(v[ix]*El);
	}
	else{
		LL mx=0;
		ForInc(i,0,El){
			int nE=((El-i+R)<=E)?(El-i+R):E;
			mx=max(mx,(LL)(v[ix]*i)+solve(ix+1,nE));
		}
		return dp[ix][El]=mx;
	}
}
int main(){
	int T;ip(T);
	for(int cs=1;cs<=T;++cs){
		ip(E);ip(R);ip(N);
		ForInc(i,0,N)ForInc(j,0,E)dp[i][j]=-1;
		ipArray(v,N);
		LL ans=solve(0,E);
		printf("Case #%d: %lld\n",cs,ans);
	}
	return 0;
}

