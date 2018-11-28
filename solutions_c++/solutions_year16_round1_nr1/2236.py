#include <string>
#include <iostream>
#include <cstdio>
using namespace std;
int test = 0;
void solve()
{
	test++;
	string s; cin >> s;
	string ss; ss.push_back(s[0]);
	for( int i = 1 ; i < s.length() ; i++ )
	{
		if(s[i] < ss[0])
		{
			ss.push_back(s[i]);
		}
		else
		{
			ss = s[i] + ss;
		}
	}
	cout << "Case #" << test << ": " << ss << endl;
	return;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t; scanf("%d\n",&t);
	while(t--)
	{
		solve();
	}
	return 0;
}