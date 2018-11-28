#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <map>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define EKLE(str,s) { qstr.push(str); qs.push(s); }
#define BAK(str,s)  { str = qstr.front(); s = qs.front(); qstr.pop(); qs.pop(); }
#define MAXN 10005
using namespace std;
typedef pair < int , int > pii;
map < string , bool > mp;
pii P[MAXN];
int N;
int A[MAXN];
bool control(string str)
{
	int i,k(0);
	for(i = 1; i < str.size(); i++)
		if( str[i] < str[i-1] )
		{
			k = i;
			break;
		}
	if( i == (int) str.size() ) return true;
	for(i = k+1; i < str.size(); i++)
		if( str[i] > str[i-1] )
			return false;
	return true;
}
void solve( int test )
{
	mp.clear();
	queue < string > qstr;
	queue < int > qs;
	int a,i,j;
	scanf("%d" , &N );
	FOR(i,1,N)
	{
		scanf("%d" , &a );
		P[i] = make_pair( a , i );
	}

	if( N < 3 ) { printf("0\n"); return; }

	sort( P+1 , P+N+1 );

	FOR(i,1,N)
		A[ P[i].s ] = i - 1;

	string str = "";

	FOR(i,1,N) str += A[i] + '0';

	mp[str] = true;

	int s;

	EKLE(str,0);

	while( !qs.empty() )
	{
		BAK(str,s);
		if( control(str) ) { printf("%d\n" , s ); return; }
		for(i = 1; i < str.size(); i++)
		{
			swap( str[i-1] , str[i] );
			if( !mp[str] )
			{
				EKLE(str,s+1);
				mp[str] = true;
			}
			swap( str[i-1] , str[i] );
		}
	}

}
int main()
{
	int T,i;
	scanf("%d" , &T );
	FOR(i,1,T)
	{
		printf("Case #%d: " , i );
		solve(i);
	}
	return 0;
}
