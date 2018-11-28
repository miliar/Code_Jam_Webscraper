#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
using namespace std;
int test = 0;
int st[111];
void solve()
{
	memset(st,0,sizeof(st));
	test++;
	string s;
	cin >> s;
	int n = s.length();
	for( int i = 0 ; i < n ; i++ )
	{
		if(s[i]=='+') st[i] = 1;
	}
	int ans = 0;
	int temp = st[0];
	for( int i = 1 ; i < n ; i++ )
	{
		if(temp!=st[i])
		{
			temp = 1-temp;
			ans++;
		}
	}
	if(temp==0) ans++;
	cout << "Case #" << test << ": " << ans << endl;
	return;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	scanf("%d\n",&t);
	while(t--)
	{
		solve();
	}
	return 0;
}