#include <bits/stdc++.h>
#include <fstream>
using namespace std;
char s[200];
int main()
{
	//ifstream cin("B-large.in");
	//ofstream cout("B-large.out");
	int t;
	cin>>t;
	for (int cas=1;cas<=t;cas++)
	{
		cin>>s;
		int len=strlen(s);
		int ans=0;
		char temp=s[0];
		for (int i=0;i<len;i++)
		{
			if (temp==s[i])
				continue;
			else
			{
				temp=s[i];
				ans++;
			}
		}
		if (temp=='-')
			ans++;
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}