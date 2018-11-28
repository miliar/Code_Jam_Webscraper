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

int main(){
	int T;ip(T);LL r,t;
	for(int cs=1;cs<=T;++cs){
		ipLL(r);ipLL(t);
		LL ans=0,i=r,n=t;
		while(n>=0){
			n-=(i+1)*(i+1)-i*i;
			if(n>=0)ans++;
			i+=2;
		}
		printf("Case #%d: %lld\n",cs,ans);
		
	}
	return 0;
}

