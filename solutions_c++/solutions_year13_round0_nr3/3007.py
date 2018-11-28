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

int		num[20],len;
bool	ok( LL x ){
	len = 0;
	while ( x ) {
		num[len++] = x%10;
		x /= 10;
	}
	Rep(i,len) if ( num[i] != num[len-1-i] ) return false;
	return true;
}

int		main(){
	int cas , tt = 0;
	scanf("%d", &cas );
	while ( cas -- ) {
		LL	l, r;
		scanf("%lld%lld", &l, &r );
		LL ans = 0;
		for(LL i = 1; sqr(i)<=r; i++){
			if ( sqr(i)<l ) continue;
			if ( ok(i) && ok(sqr(i)) ) ans ++;
		}
		printf("Case #%d: %lld\n" ,++tt, ans );
	}
	return 0;
}
