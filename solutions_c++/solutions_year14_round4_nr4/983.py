#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define MAXN 1005
using namespace std;
typedef pair < int , int > pii;
set < string > st[MAXN];
string str[MAXN];
int M,N,maxi,t;
int C[MAXN];
void dene()
{
	int i,j;
	FOR(i,1,N) st[i].clear();
	string tmp;
	FOR(i,1,M)
	{
		tmp = "";
		st[ C[i] ].insert( tmp );
		for(j = 0; j < str[i].size(); j++)
		{
			tmp += str[i][j];
			st[ C[i] ].insert( tmp );
		}
	}

	int s(0);

	FOR(i,1,N)
	{
		if( st[i].empty() ) return;
		s += (int) st[i].size();
	}
	if( s > maxi )
	{
		maxi = s;
		t = 0;
	}
	if( s == maxi ) t++;

}
void rec(int x)
{
	if(x == M + 1)
	{
		dene();
		return;
	}
	int i;
	FOR(i,1,N)
	{
		C[x] = i;
		rec(x+1);
	}
}
void solve()
{
	int i;
	scanf("%d %d" , &M , &N );
	FOR(i,1,M) cin >> str[i];

	rec(1);

	printf("%d %d\n" , maxi , t );

	maxi = 0; t = 0;

}
int main()
{
	int T,i;
	scanf("%d" , &T );
	FOR(i,1,T)
	{
		printf("Case #%d: " , i );
		solve();
	}
	return 0;
}
