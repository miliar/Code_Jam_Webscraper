//TAG : 

#include <process.h>
#include <windows.h>
#include <ctime>
#include <fstream>

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include<stack>
#include<map>
#include<queue>
#include<algorithm>
#include <climits>
#include<cassert>
#include<cctype>
using namespace std;

#define rep(i,n)	for(int (i)=0;(i)<(n);(i)++)
#define repd(i,n)	for(int (i)=(n)-1;(i)>=0;(i)--)
#define REP(i,n) for (int (i)=0,_n=(n); (i) < _n; (i)++)
#define FOR(i,a,b) for (int _b=(b), (i)=(a); (i) <= _b; (i)++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset((x),0,sizeof(x));
#define CLEARA(x) memset(&(x),0,sizeof(x));
#define FILL(x,v) memset((x),(v),sizeof(x));
#define FILLA(x,v) memset(&(x),(v),sizeof(x));

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define X first
#define Y second
#define pb push_back
#define MP make_pair
#define EPS 1e-9

#define PII pair<int,int> 
#define VI vector<int>
#define LL long long
template<typename T> inline T		gcd(T a, T b){if(a>b)swap(a,b);while(a!=0){b%=a;swap(a,b);}return b;}
template<typename T> inline T		lcm(T a, T b){return a/gcd(a,b)*b;}
//int pow(int a,int b){int c=1;while(b--)c*=a;return c;}

#ifdef _MSC_VER
#include <intrin.h>
int ctz(unsigned v){
	unsigned long index = -1;
	if (_BitScanForward(&index, v))
		return index;
	else{
		// This is undefined, I better choose 32 than 0
		return 32;
	}
}
int clz(unsigned v){
	unsigned long index=-1;
	if(_BitScanReverse(&index,v))
		return 31-index;
	else{
		// This is undefined, I better choose 32 than 0
		return 32;
}
}
#define popcnt(x) __popcnt(x)
#else
#define popcnt(x) 	__builtin_popcount(x)
#define popcntll(x) __builtin_popcountll(x)
#define ctz(x)		__builtin_ctz(x)
#define clz(x)		__builtin_clz(x)
#endif

int main(){
	char S[1001];
	int TC;
	scanf("%d", &TC);
	FOR(T, 1, TC){
		int s_max,ans=0,acc=0;
		scanf("%d %s", &s_max, S);
		FOR(i, 0, s_max){
			if (S[i] > '0' && acc<i){
				ans += i - acc;
				acc = i;
			}
			acc += S[i] - '0';
			if (acc >= 9)break;
		}
		printf("Case #%d: %d\n",T,ans);
	}

	return 0;
}