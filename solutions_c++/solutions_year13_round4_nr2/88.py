//By Lin
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<cctype>
#include<cmath>

#define eps 1e-9
#define N 100010
#define sqr(x) ((x)*(x))
#define Rep(i,n) for(int i = 0; i<n; i++)
#define foreach(i,n) for( __typeof(n.begin()) i = n.begin(); i!=n.end(); i++)
#define X first
#define Y second
#define mp(x,y) make_pair(x,y)

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

int		n;
LL		p;

bool	panA(LL x){
	LL	g = x, left = p , tol = 1ll<<n ;
	while ( left > 0 && g ){
		g = (g-1)/2;
		tol /= 2;
		left -= tol;
	}
	return left > 0;
}
bool	panB(LL x){
	LL	g = (1ll<<n)-x-1 , tol = 1ll<<n ;
	while ( g ){
		g = (g-1)/2;
		tol /= 2;
	}
	return tol <= p;
}

LL		solveA(){
	LL	g = 0 , h = (1ll<<n)-1, ans = 0;
	while ( g <= h ){
		LL	mid = ( g + h )/2;
		if ( panA(mid) ) ans = mid , g = mid+1;
		else h = mid-1;
	}
	return ans;
}
LL		solveB(){
	LL	g = 0 , h = (1ll<<n)-1, ans = 0;
	while ( g <= h ){
		LL	mid = ( g + h )/2;
		if ( panB(mid) ) ans = mid , g = mid+1;
		else h = mid-1;
	}
	return ans;
}
int		main(){
	int cas , tt = 0;
	scanf("%d", &cas );
	while ( cas -- ){
		scanf("%d%lld", &n, &p );
		printf("Case #%d: %lld %lld\n" , ++tt , solveA() , solveB() );
	}
	return 0;
}
