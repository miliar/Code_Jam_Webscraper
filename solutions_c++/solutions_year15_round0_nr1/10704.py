#include <iostream>
#include <stdio.h>
#include <string.h>

int main()
{
	int t,ptr=1;
	scanf("%d",&t);
	while(t--)
	{
		int s_max,i;
		char str[1004];

		scanf("%d%s",&s_max,str);

		long long int res,cnt;

		res=0;
		cnt=0;

		cnt=cnt+(str[0]-48);

		for(i=1;i<=s_max;i++)
		{
			if(cnt>=i && str[i]!='0')
			{
				cnt=cnt+(str[i]-48);
			}
			else
			{
				if(str[i]!='0')
				{
					res=res+(i-cnt);
					cnt=cnt+res+(str[i]-48);
				}
			}
		}

		printf("Case #%d: %lld\n",ptr,res);
		ptr++;

	}

	return 0;
}