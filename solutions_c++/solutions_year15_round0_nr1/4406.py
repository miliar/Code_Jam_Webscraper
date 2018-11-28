#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s;
	int t, ans, st, m;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		ans = 0;
		st = 0;
		cin>>m>>s;
		for(int j=0;j<m+1;j++)
		{
			if(st < j)
			{
				ans += j-st;
				st = j;
			}
			st += s[j]-'0';
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
