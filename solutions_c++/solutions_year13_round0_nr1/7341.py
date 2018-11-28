#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		char a[10][10];
		int ans=0;
		for(int j=0;j<4;j++)
		{
			scanf("%s",a[j]);
		}
		int dot=0;
		for(int j=0;j<4;j++)
		{
			int co=0,cx=0;
			for(int k=0;k<4;k++)
			{
				if(a[j][k]=='O' || a[j][k]=='T')co++;
				if(a[j][k]=='X' || a[j][k]=='T')cx++;
				if(a[j][k]=='.')dot++;
			}
			if(co==4)
			{
				ans=1;
				break;
			}
			else if(cx==4)
			{
				ans=2;
				break;
			}
		}
		for(int j=0;j<4 && ans==0;j++)
		{
			int co=0,cx=0;
			for(int k=0;k<4;k++)
			{
				if(a[k][j]=='O' || a[k][j]=='T')co++;
				if(a[k][j]=='X' || a[k][j]=='T')cx++;
			}
			if(co==4)
			{
				ans=1;
				break;
			}
			else if(cx==4)
			{
				ans=2;
				break;
			}
		}
		if(ans==0)
		{
			int co=0,cx=0;
			for(int j=0;j<4;j++)
			{
				if(a[j][j]=='O' || a[j][j]=='T')co++;
				if(a[j][j]=='X' || a[j][j]=='T')cx++;
			}
			if(co==4)
			{
				ans=1;
			}
			else if(cx==4)
			{
				ans=2;
			}
		}
		if(ans==0)
		{
			int co=0,cx=0;
			for(int j=0;j<4;j++)
			{
				if(a[j][3-j]=='O' || a[j][3-j]=='T')co++;
				if(a[j][3-j]=='X' || a[j][3-j]=='T')cx++;
			}
			if(co==4)
			{
				ans=1;
			}
			else if(cx==4)
			{
				ans=2;
			}
		}
		printf("Case #%d: ",i);
		if(ans==1)
		{
			printf("O won\n");
		}
		else if(ans==2)
		{
			printf("X won\n");
		}
		else if(ans==0 && dot==0)
		{
			printf("Draw\n");
		}
		else
		{
			printf("Game has not completed\n");
		}	
	}
	return 0;
}