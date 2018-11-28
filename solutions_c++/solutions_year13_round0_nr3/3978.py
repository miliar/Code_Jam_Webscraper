// Author: Nishant R. Krishan
#include <iostream>
#include <sstream>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <deque>
#include <bitset>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <vector>
#include <queue>

using namespace std;

#define VI vector < int >
#define VVI(A,N,M) vector< VI > A( N, VI (M) )
#define LL long long
#define LLU unsigned long long
#define SI ({int x;scanf("%d",&x);x;})
#define SC ({char x;scanf("%c",&x);x;})
#define SLL ({LL x;scanf("%lld",&x);x;})
#define SLLU ({LLU x;scanf("%llu",&x);x;})
#define PI acos(-1)
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int) (x).size()) 
#define SORT(c) sort(all(c)) 
#define FIT(it,v) for (typeof(v.begin()) it = v.begin(); it != v.end(); it++)
#define FITD(it,v) for (typeof(v.rbegin()) it = v.rbegin(); it != v.rend(); it++)
#define IATOV(a) ({vector<int> v(a,a+sizeof(a)/sizeof(int));v;})
#define CATOV(a) ({vector<char> v(a,a+sizeof(a)/sizeof(char));v;})
#define sieve(a) ({int b=ceil(sqrt(a));VI d(a,0);VI e;int f=2;e.pb(2);e.pb(3);for(int x=1;x<b+1;x++){for(int y=1;y<b+1;y++){int n=(4*x*x)+(y*y);if(n<=a&&(n%12==1||n%12==5)){d[n]^=1;}n=(3*x*x)+(y*y);if(n<=a&&n%12==7){d[n]^=1;}n=(3*x*x)-(y*y);if(x>y&&n<=a&&n%12==11){d[n]^=1;}}}for(int r=5;r<b+1;r++){if(d[r]){for(int i=r*r;i<a;i+=(r*r)){d[i]=0;}}}for(int c=5;c<a;c++){if(d[c]){e.pb(c);}}e;})
#define INF 1000000007
#define EPS 1e-9

/********************************************************************************************************************************/

string convertToString( LL X ){
	string res="", temps;
	while( X!=0 ){
		temps = X%10 + '0';
		res = temps + res;
		X /= 10;
	}
	return res;
}

bool checkPalindrome( string X ){
	LL i, L = X.size();
	for( i=0;i<=(L-1-i);++i ){
		if( X[i]!=X[L-1-i] )
			return false;
	}
	return true;
}

vector<LL> Sieve;

LL getLessThan( LL X ){
	LL i, L;
	L = Sieve.size();
	LL mysum=0;
	for( i=0;i<L;++i )
	{
		if( Sieve[i]>=X )
			break;
	}
	return i;
}

void fillSieve(){
	LL i;
	Sieve.clear();
	for( i=1;i*i<=1e14;++i ){
		if( checkPalindrome(convertToString(i)) && checkPalindrome(convertToString(i*i)) )
			Sieve.push_back(i*i);
	}
}

int main(int argc, char** argv){
	fillSieve();	
	LL T=SLL, t, A, B;
	for( t=1;t<=T;++t ){
		A=SLL, B=SLL;
		printf("Case #%lld: %lld\n", t, getLessThan(B+1)-getLessThan(A));
	}

	return 0;
}

