#include<stdio.h>

int main()
{
	int T,S;
	char Shyness[1002];
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		scanf("%d",&S);
		scanf("%s",Shyness);

		int curAdd = 0;
		int curStanding = 0;
		for(int j=0;j<=S;j++)
		{
			if(Shyness[j] != '0')
			{
				if(curStanding >= j )
				{
					curStanding += (Shyness[j]-'0');
				}
				else
				{	
					curAdd += (j - curStanding);
					curStanding = j + (Shyness[j]-'0');
				}
			}
		}
		printf("Case #%d: %d\n",i,curAdd);
	}
	return 0;
}
