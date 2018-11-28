#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
using namespace std;
int test = 1;
int dy[101];

int c,d,v;
inline int check()
{
	for( int i = 1 ; i <= v ; i++ )
	{
		if(dy[i]==0)
			return i;
	}
	return v+1;
}
void solve()
{
	cin >> c >> d >> v;
	dy[0] = 1;
	int temp,cnt=0;
	for( int i = 0 ; i < d ; i++ )
	{
		cin >> temp;
		for( int j = v ; j >= 0 ; j-- )
		{
			if( dy[j] != 0 )
			{
				dy[j+temp] = 1;
			}
		}
	}
	int p;
	while((p=check())!=v+1)
	{
		for( int j = v ; j >= 0 ; j-- )
		{
			if( dy[j] != 0 )
			{
				dy[j+p] = 1;
			}
		}
		cnt++;
	}
	printf("Case #%d: %d\n",test++,cnt);
	return;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int t;
	cin >> t;
	while(t--)
	{
		memset(dy,0,sizeof(dy));
		solve();
	}
	return 0;
}