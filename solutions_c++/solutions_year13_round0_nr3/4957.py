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
#include <iomanip>
#include <locale>
#include <sstream>
#include <string>
template<typename T> T gcd(T a, T b) { return (b == 0) ? abs(a) : gcd(b, a % b); }
template<typename T> inline T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<typename T> inline T mod(T a, T b) { return (a % b + b) % b; }
template<typename T> inline T sqr(T x) { return x * x; }
#define tostring(x) static_cast<ostringstream*>( &(ostringstream() << x) )->str();
typedef long long LL;
using namespace std;



/* Main Code starts here :) */
bool palin(LL x){
	string str=tostring(x);
	int sz=str.size();
	ForInc(i,0,sz/2)if(str[i]!=str[sz-1-i])return false;
	return true;
}
LL solve(LL a, LL b){
	LL res=0;
	for(LL i=a;i<=b;++i){
		if(palin(i)){
			LL root=sqrt(i);
			if(root*root==i){
				if(palin(root))res++;
			}
		}
	}
	return res;
}
int main(){
	int t;ip(t);
	LL a,b;
	ForInc(cs,1,t){
		ipLL(a);ipLL(b);
		printf("Case #%d: %lld\n",cs,solve(a,b));	
	}
	return 0;
}
