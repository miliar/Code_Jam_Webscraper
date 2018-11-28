#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,cs=0,i;
	char str[1009];
	scanf("%d",&t);
	while(t--)
	{
		cs++;
		scanf("%s",str);
		char mx ='A';
		list<char> ans;
		int n = strlen(str);
		for(i=0;i<n;i++)
		{
			mx = mx<str[i]?str[i]:mx;
		}
		char cur = str[0];
		ans.push_back(str[0]);
		int allright = 0;
		if(str[0]==mx)
			{
				allright =1;
			}
		
		for(i=1;i<n;i++)
		{
			if(str[i]==mx)
			{
				allright =1;
				ans.push_front(str[i]);
				continue;
			}
			if(allright)
			{
				ans.push_back(str[i]);
				//cur = str[i];
				continue;
			}
			else
			{
				if(str[i]>=*ans.begin())
				{
					ans.push_front(str[i]);
					continue;
				}
				else
				{
					ans.push_back(str[i]);
					//cur = str[i];
					continue;
				}
			}

		}
		char fans[1009];
		n=0;
		for(list<char>::iterator it = ans.begin();it!=ans.end();++it)
		{
			fans[n] = *it;
			n++; 
		}
		fans[n] = '\0';
		printf("Case #%d: %s\n",cs,fans);


	}
}