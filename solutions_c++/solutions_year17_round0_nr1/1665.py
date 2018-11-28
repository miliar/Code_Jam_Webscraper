#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		char input[1005];
		int k;

		scanf("%s %d",input,&k);

		int len=strlen(input);

		int count=0;
		for(int i=0;i<=len-k;i++)
		{
			if(input[i]=='-')
			{
				count++;
				for(int j=i;j<i+k;j++)
				{
					if(input[j]=='+')
						input[j]='-';
					else if(input[j]=='-')
						input[j]='+';
				}
			}
		}

		int flag=1;

		for(int i=len-k;i<len;i++)
		{
			if(input[i]=='-')
			{
				flag=0;
				break;
			}
		}

		if(flag)
			printf("Case #%d: %d",t,count);
		else
			printf("Case #%d: IMPOSSIBLE",t);

		if(t!=T) printf("\n");


	}
	return 0;
}