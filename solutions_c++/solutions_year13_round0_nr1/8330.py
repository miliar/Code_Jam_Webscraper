#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;	
int main()
{
	int t,i,cases,sum[4],dia[4],count,k,j,flag;
	char s[5][5];
	scanf("%d",&cases);
	for(t=1;t<=cases;t++)
	{
		for(i=0;i<4;i++)
			scanf("%s",&s[i]);
		dia[0]=0;dia[1]=0;dia[2]=0;dia[3]=0;count=0;
		flag=0;
		for(i=0,k=3;i<4;i++,k--)
		{
			sum[0]=0;sum[1]=0;sum[2]=0;sum[3]=0;
			for(j=0;j<4;j++)
			{
				if(s[i][j]=='X'||s[i][j]=='T')
					sum[0]++;
				if(s[i][j]=='O'||s[i][j]=='T')
					sum[1]++;
				if(s[j][i]=='X'||s[j][i]=='T')
					sum[2]++;
				if(s[j][i]=='O'||s[j][i]=='T')
					sum[3]++;
				if(s[i][j]=='.')
					count++;
			}
			if(s[i][i]=='X'||s[i][i]=='T')
					dia[0]++;
			if(s[i][i]=='O'||s[i][i]=='T')
					dia[1]++;
			if(sum[0]==4||sum[2]==4)
				{printf("Case #%d: X won\n",t);flag=1;break;}
			if(sum[1]==4||sum[3]==4)
				{printf("Case #%d: O won\n",t);flag=1;break;}
			if(s[i][k]=='X'||s[i][k]=='T')
					dia[2]++;
			if(s[i][k]=='O'||s[i][k]=='T')
					dia[3]++;

		}
		if(dia[0]==4||dia[2]==4)
			{printf("Case #%d: X won\n",t);flag=1;}
		if(dia[1]==4||dia[3]==4)
			{printf("Case #%d: O won\n",t);flag=1;}
		if(flag==0 && count>0)
			{printf("Case #%d: Game has not completed\n",t);}
		if(flag==0 && count==0)
			{printf("Case #%d: Draw\n",t);}
	}
	return 0;
}