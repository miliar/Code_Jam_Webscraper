#include <iostream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <cctype>
#include <queue>
#include <numeric>
#include <cmath>
#define repn(a,x,y) for (int a=x; a<y; a++)
#define rep(a, n ) repn( a , 0 , n ) 
#define fd(a,x,y) for (int a=x; a>=y; a--)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define vint vector<int>
#define pb push_back
#define FOR(it,A) for (typeof A.begin() it=A.begin(); it!=A.end(); it++)
#define ones(x) __builtin_popcountll(x)
#define clr(A,x) memset (A, x, sizeof A)
#define eps (1e-9)
#define cua(x) (x)*(x)
#define fst first
#define snd second
#define pii pair<int,int>
#define debug(x) cout << #x << " = " << x <<endl
typedef long long ll;
using namespace std;
vector<ll> v;
bool pal( ll n ){
	ll r = 0, N = n;
	while(n){
		r = 10*r + n%10;
		n /=10;
	}

	return r == N;
}
void pre(){
	for( ll i = 1; i < 10000007; i++){
		if ( pal( i ) && pal(i*i) ) v.push_back( i*i );
	}
}
int main(){
	int runs;
	pre();
	scanf("%d",&runs);
	for( int r = 1; r <= runs;r++){
		ll a,b;
		scanf("%lld %lld",&a, &b );
		printf("Case #%d: %d\n",r,upper_bound(all(v),b )-
		upper_bound(all(v),a-1) );
	}

	return 0;
}
