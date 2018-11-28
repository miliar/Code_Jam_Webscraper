#include <cstdio>
#include <iostream>
using namespace std;

int i, n=10000000;
int nr, t, T, Rez[205];
long long x, y;
int rez;

bool palindrom( long long nr ){
	long long c=nr, rez=0;
	while( nr ){
		rez *= 10;
		rez += nr%10;
		nr /=10;
	}
	return rez == c;
}

int bs( long long val ){
	int rez=0, p;
	for( p=1; p<=nr; p<<=1 )
		;
	for( ; p; p>>=1 )
		if( rez+p <= nr && Rez[rez+p] <= val )
			rez+=p;
	return rez;
}
int main(){
	freopen("date.in","r",stdin);
	freopen("date.out","w",stdout);
	for( i=1; i<=n; ++i )
		if( palindrom(i) && palindrom(1LL*i*i) ){
			Rez[++nr]=1LL*i*i;
		}
	scanf("%d", &T );
 	for( t=1; t<=T; ++t ){
		scanf("%lld %lld", &x, &y );
		x--;
		rez = bs(y);
		rez -= bs(x);
		printf("Case #%d: %d\n",t,rez);
	}
	return 0;
}
