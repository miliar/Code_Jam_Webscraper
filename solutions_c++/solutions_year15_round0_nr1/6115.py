#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int j=1;j<=t;j++)
	{
		int sz;
		scanf("%d",&sz);
		string s;
		cin>>s;
		int needed=0,standing=0,temp,te;
		for(int i=0;i<=sz;i++)
		{
			temp=s[i]-'0';
			if(temp!=0)
			{
				if(standing>=i)
					standing+=temp;
				else
				{
					te=i-standing;
					needed+=te;
					standing+=(te+temp); 
				}
			}
		}
		printf("Case #%d: %d\n",j,needed);
	}
	return 0;
}	
