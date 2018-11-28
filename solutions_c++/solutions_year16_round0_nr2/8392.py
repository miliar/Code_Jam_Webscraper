#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,i;
	scanf ("%d",&t);
	int t1 = t;
	while(t--)
	{
		string s;
		cin>>s;
		int a[100002];
		int ans = 0;
		int prev = 0;
		for(i=0;i<s.length();i++)
		{
			if(s[i]=='+')
				a[i] = 0;
			else
				a[i] = 1;
		}
		if(a[s.length()-1]==0)
		{
			ans = 0;
			prev = 0;
		}
		else
		{
			ans = 1;
			prev = 1;
		}
		for(i=s.length()-2;i>=0;i--)
		{
			if(a[i]==prev)
				continue;
			ans++;
			prev = prev^1;
		}
		printf("Case #%d: ",t1-t);
		printf("%d\n",ans);
	}
	

	return 0;
}