#include<bits/stdc++.h>
using namespace std;

char str[2001];

int main()
{
	int t,persons,ans,smax;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++)
	{
		scanf("%d",&smax);
		scanf("%s",str);

		persons=0;ans=0;
		for(int i=0;i<=smax;i++)
		{
			//this is shyness i.. means ppl in this category require at least i ppl before them to have stood up..
			if(str[i]=='0')
				continue;
			if(i>persons)
			{
				ans+=i-persons;
				persons=i;
			}
			persons+=str[i]-'0';
		}

		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
			
