//{{{
#define DEF
#ifdef DEF
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <stack>
#include <vector>
#include <list>
#include <map>
#include <cctype>
#include <queue>
#include <cstring>
#include <cmath>
#include <set>
#include <deque>


//-----------------------------------------------------


using namespace std;
typedef unsigned int uint;
typedef long long int llint;
typedef unsigned long long int ullint;

typedef pair<int,int> Pii;
typedef pair<llint,llint> Pll;

#define mrepp(i,n,x)  for(int i = n-1; i >= x; i--)
#define mrep(i,n) mrepp(i,n,0)
#define repp(i,x,n)  for(unsigned int i = x; i < n; i++)
#define rep(i,n) repp(i,0,n)
#define pb        push_back
#define all(vec)  (vec).begin(),(vec).end()
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
//#define reach(i,c) for(__typeof((c).rbegin()) i=(c).rbegin();i!=(c).rend();i++)
#define fst         first
#define scd         second

#define sz(v)     ((llint)(v).size())
//#define bit(n)    (1ll<<(li)(n))
//#define mkP        make_pair
#include <assert.h>

//-----------------------------------------------------
#endif
//}}}



llint is_prime(ullint n){
	ullint i;
	assert( n > 1 );
	
	if( n < 2 ){
		return -1;
	}else if( n == 2 ){
		return 2;
	}
	
	if( n % 2 == 0 ){
		return 2;
	}
	
	for( i = 3; i<= n/i ; i += 2 ){
		if( n % i == 0 ){
			return i;
		}
	}
	return -1;
}

ullint change_base(unsigned x,char base){
	ullint ret = 0;
	ullint rank = 1;
	rep(i,32){
		ret += ( x & 0x1 ) * rank;
		x = x >> 1;
		rank *= base;
	}
	return ret;
}

int main(){
	unsigned int T;
	cin >> T;
	rep(t,T){
		int N,J;
		int anscnt = 0;
		cin >> N >> J;
		printf("Case #%d:\n",t+1);
		rep(i,1<<(N-2)){
			unsigned x = i;
			x = x << 1;
			x |= ( 0x1 | ( 0x1 << (N-1) ) );
			
			//fprintf(stderr,"0x%x\n",x);
			llint divs[12];
			repp(b,2,11){
				ullint bx = change_base(x,b);
				divs[b] = is_prime( bx );
				//fprintf(stderr,"  base[%2d] : %lld ( %lld )\n",b,bx,divs[b]);
				if( divs[b] < 0 ){ break; }
				if( b == 10 ){
					//fprintf(stderr,"found!\n");
					printf("%lld ",bx);
					repp(k,2,11){ printf("%lld%c",divs[k],(k==10?'\n':' ')); }
					anscnt++;
				}
			}
			if( anscnt == J ){ break; }
		}
	}
	return 0;
}
