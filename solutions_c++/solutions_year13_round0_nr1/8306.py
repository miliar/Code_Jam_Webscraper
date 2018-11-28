#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	int t,d,pro,pro1;
	char c,a[40][40];
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		cin>>a[i][j];
		c=a[0][0];
		if(c=='T')
		c=a[1][1];
		if(c=='.')
		pro=1;
		d=0;
		if(pro==0)
		{
			for(int i=1;i<4;i++)
			{
				if(a[i][i]==c||a[i][i]=='T')
				continue;
				else
				{
					d=1;
					break;
				}
			}
		}
		
		if(d==0&&pro==0)
		{
			printf("Case #%d: %c won\n",i,c);
			continue;
		}
		else if(pro==1||d==1)
		{
			pro1=0;
			d=0;
			c=a[0][3];
			if(c=='T')
			c=a[1][2];
			if(c=='.')
			{
				pro=1;
				pro1=1;
			}
			d=0;
			if(pro1==0)
			{
				for(int i=1;i<4;i++)
				{
					if(a[i][4-i-1]==c||a[i][4-i-1]=='T')
					continue;
					else
					{
						d=1;
						break;
					}
				}
			}
		}
		
		if(d==0&&pro1==0)
		{
			printf("Case #%d: %c won\n",i,c);
			continue;
		}
		else if(d==1||pro1==1)
		{
			for(int i=0;i<4;i++)
			{
				c=a[i][0];
				if(c=='T')
				c=a[i][1];
				if(c=='.')
				{
					pro=1;
					d=1;
				}
				else
				{
					d=0;
					for(int j=1;j<4;j++)
					{
						if(c==a[i][j]||a[i][j]=='T')
						continue;
						else
						{
							d=1;
							break;	
						}
					}
				}
				if(d==0)
				break;
				
				c=a[0][i];
				//cout<<c<<endl;
				if(c=='T')
				c=a[1][i];
				if(c=='.')
				{
					pro=1;
					d=1;
					//continue;
				}
				else
				{
					d=0;
					for(int j=1;j<4;j++)
					{
						if(c==a[j][i]||a[j][i]=='T')
						continue;
						else
						{
							d=1;
							break;	
						}
					}
				}
				if(d==0)
				{
					//cout<<"ok"<<endl;
					break;
					
				}
				
			}
		}
		if(d==0)
		printf("Case #%d: %c won\n",i,c);
		else if(d==1&&pro==0)
		printf("Case #%d: Draw\n",i);
		else if(d==1&&pro==1)
		printf("Case #%d: Game has not completed\n",i);
		
		
		
	}
	return 0;
}
