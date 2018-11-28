#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("D://B.in","r",stdin);
	freopen("D://Bsmall.out","w",stdout);
	int test=0,t;
	scanf("%d",&t);
	while(test!=t)
	{
		string s;
		cin>>s;
		if(s.length()==1)
		{
			if(s[0]=='-')
				printf("Case #%d: %d\n",test+1,1);
			else
				printf("Case #%d: %d\n",test+1,0);
		}
		else
		{
			char check=s[0],first,last;
			int change=0,i;
			first=s[0];
			last=s[s.length()-1];
			for(i=1;i<s.length();i++)
			{
				if(check!=s[i])
				{
					change++;
					check=s[i];
				}
			}
			if(change==0)
			{
				if(first=='-')
				{
					printf("Case #%d: %d\n",test+1,1);
				}
				else
				{
					printf("Case #%d: %d\n",test+1,0);
				}
			}
			else
			{
				if(last=='+')
				{
					printf("Case #%d: %d\n",test+1,change);
				}
				else
				{
					printf("Case #%d: %d\n",test+1,change+1);
				}
			}
			
		}
		test++;
	}
}
