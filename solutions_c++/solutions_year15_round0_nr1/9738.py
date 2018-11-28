#include<conio.h>
#include<stdio.h>
#include<stdlib.h>
void main()
{
	clrscr();
	freopen("input.in","r",stdin);
	freopen("murali.txt","w",stdout);
	int t,num[100][7],y[100],n[100],sum,temp;
	long tmp;
	scanf("%d\n",&t);
	for(int i=0;i<t;i++)
	{
		scanf("%d",&n[i]);
		scanf("%lu",&tmp);
		for(int j=n[i];j>=0;j--)
		{
			num[i][j]=tmp%10;
			tmp=tmp/10;
		}
	}
	for(i=0;i<t;i++)
	{
		y[i]=0;
		sum=0;
		temp=0;
		for(int j=0;j<=n[i];j++)
		{
			if((sum<j+1)&&(num[i][j]!=0))
			{
				temp=j-sum;
				y[i]=y[i]+temp;
				sum=sum+temp;
			}
			sum=sum+num[i][j];
		}
	}
	for(i=0;i<t;i++)
	{
		printf("Case #%d: %d\n",i+1,y[i]);
	}
}
