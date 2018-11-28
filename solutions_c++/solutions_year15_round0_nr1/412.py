#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
int t=1;
int res; 
void solve()
{
	int n,temp;
	int cnt;
	string s;
	res = 0;
	cin >> n >> s;
	cnt = s[0]-'0';
	for( int i = 1 ; i < n+1 ; i++ )
	{
		temp = s[i]-'0';
		if( i > cnt )
		{
			res += i-cnt;
			cnt = i;
		}
		cnt += temp;
	}
	cout << "Case #" << t << ": " << res << endl;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tt;
	cin >> tt;
	for(t=1;t<=tt;t++)
	{
		solve();
	}
	return 0;
}