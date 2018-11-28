#include <iostream>
#include <cstdio>

using namespace std;
char c[4][4];
int count1,count2,count3;
int func()
{
    	int flag=0,win=-1;
		
		if(count1==0)
		{
			if(count2==3 && count3==1)
			{
				flag=1;
				win=0;
			}
			
			else if(count2==4)
			{
				flag=1;
				win=0;
				
			}
		}
		
		if(count2==0)
		{
			if(count1==3 && count3==1)
			{
				flag=1;
				win=1;
			}
			
			else if(count1==4)
			{
				flag=1;
				win=1;
				
			}
		}
		if(flag)
		{
			if(win)
				return 1;
			else
				return 0;
		}
		else
			return -1;
}
int main()
{
	int t,i,j,k,flag,top,bottom,left,right,diag1,diag2;
	char x;
	
	scanf("%d\n",&t);
	for(k=1;k<=t;k++)
	{
		for(i=0;i<4;i++)
		{
				for(j=0;j<4;j++)
				{
					scanf("%c",&c[i][j]);
				}
				scanf("\n");
		}
	
		flag=0;
		for(i=0;i<4;i++)
		{
			count1=0;
			count2=0;
			count3=0;
			for(j=0;j<4;j++)
			{
				if(c[i][j]=='X')
					count1++;
				else if(c[i][j]=='O')
					count2++;
				else if(c[i][j]=='T')
					count3++;
			}
			bottom=func();
			if(bottom==1)
			{
				printf("Case #%d: X won\n",k);
				flag=1;
				break;
			}
			else if(bottom==0)
			{
				printf("Case #%d: O won\n",k);
				flag=1;
				break;
			}
		
		}
		
		if(flag)
			continue;
			
		flag=0;
		for(j=0;j<4;j++)
		{
			
			count1=0;
			count2=0;
			count3=0;
			for(i=0;i<4;i++)
			{
				if(c[i][j]=='X')
					count1++;
				else if(c[i][j]=='O')
					count2++;
				else if(c[i][j]=='T')
					count3++;
			}
			left=func();
			if(left==1)
			{
				printf("Case #%d: X won\n",k);
				flag=1;
				break;
			}
			else if(left==0)
			{
				printf("Case #%d: O won\n",k);
				flag=1;
				break;
			}
		}
		
		if(flag)
			continue;
		
		count1=0;
		count2=0;
		count3=0;
		for(i=0;i<4;i++)
		{
			if(c[i][i]=='X')
				count1++;
			else if(c[i][i]=='O')
				count2++;
			else if(c[i][i]=='T')
				count3++;
		}
		diag1=func();
		if(diag1==1)
		{
			printf("Case #%d: X won\n",k);
			continue;
		}
		else if(diag1==0)
		{
			printf("Case #%d: O won\n",k);
			continue;
		}
		
		count1=0;
		count2=0;
		count3=0;
		for(i=0;i<4;i++)
		{
			if(c[3-i][i]=='X')
				count1++;
			else if(c[3-i][i]=='O')
				count2++;
			else if(c[3-i][i]=='T')
				count3++;
		}
		diag2=func();
		if(diag2==1)
		{
			printf("Case #%d: X won\n",k);
			continue;
		}
		else if(diag2==0)
		{
			printf("Case #%d: O won\n",k);
			continue;
		}
		
		
		flag=0;
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
			{
				if(c[i][j]=='.')
				{
					flag=1;
					break;				
				}
			}
			if(flag)
				break;
		}
		
		if(flag==0)
			printf("Case #%d: Draw\n",k);
		else
			printf("Case #%d: Game has not completed\n",k);
		/*for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			
			{
				cout<<c[i][j]<<" ";
			}
			cout<<"\n";
		}*/
	}
	return 0;
}
