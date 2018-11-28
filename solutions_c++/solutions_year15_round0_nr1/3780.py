#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int j=1;
	while(t--)
	{	
		int smax,i;
		scanf("%d",&smax);
		char str[1009];
		int cnt=0,c=0;
		scanf("%s",str);
		if(smax==0)
			printf("Case #%d: 0\n",j);
		if(smax >=1)
		{
			i=0;
			while(i<=smax)
			{
				if(cnt>= i)
				{
					cnt+= (str[i]-'0');
					i++;
				}
				else
				{
					c+=(i-cnt);
					cnt+= (i-cnt);
				}
			}
			printf("Case #%d: %d\n",j,c);
		}
		
		j++;
	}
	return 0;
}