#include <iostream>
#include <cstdio>
#include <cstring>
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
	printf("Case #%d: ",i); // Be careful here, some times there will be no space after ':'. So, modify this.
}

void solve(){
	char g[102], c = '+';
	scanf ("%s", g);
	int n = strlen(g), count = 0;
	for ( int i = n-1 ; i >= 0 ; i-- ){
		if ( g[i] == c ) continue;
		count++;
		c = ( c == '+' ? '-':'+');
	}
	pri("%d\n",count);
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
