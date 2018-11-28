#include <iostream>
#include <stdio.h>
int main()
{
	int t;
	scanf("%d",&t);

	for(int i=0;i<t;i++)
	{
		int s;
		char str[1002];

		scanf("%d %s",&s,str);

		int cs=(str[0]-'0');
		int add=0;

		for(int j=1;j<=s;j++)
		{
				int x=0;
				if(j>cs)
					x=(j-cs);
				cs=cs+(str[j]-'0')+x;
				add=add+x;
		}

		printf("Case #%d: %d\n",i+1,add);


	}

	return 0;
}
