#include <iostream>
#include <cstdio>
//#include<fstream>
using namespace std;
typedef long long int l;
#define f first
#define s second
#define full(p) for(it = p.begin();it!=p.end();it++)
#define FO(i,n) for (int i=0;i<n;i++)
#define pri printf

void inline prrrrrr(int i)
{
	printf("Case #%d: ",i);
}


void solve(){
//	stuff
	int n, x = 0 ; cin >> n ;
	l p = n;
	if ( !n ) { pri("INSOMNIA\n"); return; }
	for (int i = 1 ; i < 1000 ; i++, p += n ){
		for ( l k = p ; k ; k /= 10 ){
			x |= 1 << (k % 10);
		}
		if ( __builtin_popcount(x) == 10 ) { pri("%lld\n", p ); return; }
	}
	pri("INSOMNIA\n");
}
int main()
{
	int t;
	freopen("test.txt","r",stdin);
	freopen("write.txt","w",stdout);
	cin >> t;
	for( int zz = 1 ; zz <= t ; zz++ )
	{
		prrrrrr(zz);
		solve();
	}
	return 0;
}
