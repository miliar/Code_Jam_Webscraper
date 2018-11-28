#include<stdio.h>
int main(void)
{
	int t,T,i,j,CO,CX,d,com;
	char arr[5][5];

	scanf("%d",&T);

	for(t=1;t<=T;t++)
	{
		for(i=0;i<4;i++)
			scanf("%s",arr[i]);
		for(i=0;i<4;i++)
		{
			CO=0;
			CX=0;
			d=0;
			com=0;
			for(j=0;j<4;j++)
			{
				if(arr[i][j]=='O')
					CO++;
				else if(arr[i][j]=='X')
					CX++;
				else if(arr[i][j]=='T')
				{
					CX++;
					CO++;
				}
				else if(arr[i][j]=='.')
					d=1;
			}
			if(CX==4)
			{	
				printf("Case #%d: X won\n",t);
				com=1;
				break;
			}
			else if(CO==4)
			{
				printf("Case #%d: O won\n",t);
				com=1;
				break;
			}
		}
		if(com==1)
			continue;
		for(j=0;j<4;j++)
		{
			CO=0;
			CX=0;
			com=0;
			for(i=0;i<4;i++)
			{
				if(arr[i][j]=='O')
					CO++;
				else if(arr[i][j]=='X')
					CX++;
				else if(arr[i][j]=='T')
				{
					CX++;
					CO++;
				}
				else if(arr[i][j]=='.')
					d=1;
			}
			if(CX==4)
			{	
				printf("Case #%d: X won\n",t);
				com=1;
				break;
			}
			else if(CO==4)
			{
				printf("Case #%d: O won\n",t);
				com=1;
				break;
			}
		}
		if(com==1)
			continue;
		CO=0;
		CX=0;
		com=0;
		for(i=0;i<4;i++)
		{
			if(arr[i][i]=='O')
				CO++;
			else if(arr[i][i]=='X')
				CX++;
			else if(arr[i][i]=='T')
			{
				CX++;
				CO++;
			}
			else if(arr[i][i]=='.')
				d=1;
		}
		if(CX==4)
		{	
			printf("Case #%d: X won\n",t);
			continue;
		}
		else if(CO==4)
		{
			printf("Case #%d: O won\n",t);
			continue;
		}
		CO=0;
		CX=0;
		com=0;
		for(i=0;i<4;i++)
		{
			if(arr[i][3-i]=='O')
				CO++;
			else if(arr[i][3-i]=='X')
				CX++;
			else if(arr[i][3-i]=='T')
			{
				CX++;
				CO++;
			}
			else if(arr[i][3-i]=='.')
				d=1;
		}
		if(CX==4)
		{	
			printf("Case #%d: X won\n",t);
			continue;
		}
		else if(CO==4)
		{
			printf("Case #%d: O won\n",t);
			continue;
		}
		else if(d==0)
		{
			printf("Case #%d: Draw\n",t);
			continue;
		}
		else if(d==1)
		{
			printf("Case #%d: Game has not completed\n",t);
			continue;
		}
	}

	return 0;
}