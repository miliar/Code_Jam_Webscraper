#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define MAXN 105
using namespace std;
string str[MAXN] , str2[MAXN];
int N,T;
int MAX[MAXN] , MIN[MAXN];
string f(int a)
{
	string tmp;
	int i;
	tmp += str[a][0];
	for(i = 1; i < str[a].size(); i++)
		if( str[a][i] != str[a][i-1] )
			tmp += str[a][i];
	return tmp;
}
void solve()
{
	memset( MAX , 0 , sizeof MAX  );
	memset( MIN , 15 , sizeof MIN );
	int i,j,res(0),s,t;
	bool flag = false;
	scanf("%d" , &N );
	FOR(i,1,N)
	{
		cin >> str[i];
		str2[i] = f(i);
		if(i > 1 && str2[i] != str2[i-1]) flag = true;
	}
	if(flag) { printf("Fegla Won\n"); return; }

	FOR(i,1,N)
	{
		s = 1; t = 0;
		for(j = 1; j < str[i].size(); j++)
			if( str[i][j] != str[i][j-1] )
			{
				t++;
				MAX[t] = max( MAX[t] , s );
				MIN[t] = min( MIN[t] , s );
				s = 1;
			}
			else
				s++;
		t++;
		MAX[t] = max( MAX[t] , s );
		MIN[t] = min( MIN[t] , s );
	}

	FOR(i,1,t) res += MAX[i] - MIN[i];

	printf("%d\n" , res );

}
int main()
{
	freopen("inp","r",stdin);
	freopen("out.txt","w",stdout);
	int i;
	scanf("%d" , &T );
	FOR(i,1,T)
	{
		printf("Case #%d: " , i );
		solve();
	}
	return 0;
}
