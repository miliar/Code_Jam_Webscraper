#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for (int j = 1; j <= t; ++j)
	{
		printf("Case #%d: ",j);
		string s;
		cin>>s;
		int n=s.size();
		list<char>ans;
		ans.push_back(s[0]);
		for (int l = 1; l < n; ++l)
		{
			char a=ans.front();
			if(s[l]>=a)
			{
				ans.push_front(s[l]);
			}
			else
			{
				ans.push_back(s[l]);
			}
		}
		for (list<char>::iterator i = ans.begin(); i != ans.end(); ++i)
		{
			cout<<*i;	
		}
		cout<<"\n";
	}
}