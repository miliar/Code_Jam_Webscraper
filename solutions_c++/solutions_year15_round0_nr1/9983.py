#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,smax;
	char shy[1002];
	scanf("%d",&t);
	while(t-->0)
	{
		scanf("%d %s",&smax,shy);
		int p=0,ans=0;
		p=shy[0]-48;
		for(int i=1;shy[i]!='\0';i++)
		{
			if(p<i)
			{
				ans+=(i-p);
				p+=(i-p);
			}
			p+=(shy[i]-48);
		}
		printf("%d\n",ans);
	}
	return 0;
}
