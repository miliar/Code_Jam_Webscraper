#include<iostream>
#include<stdio.h>
using namespace std;

int a[10][10];
int m,n;
bool chk(int x)
{
	for(int i=0;i<n;i++)
	{
		if(a[x][i]!=1)
			return true;
	}
	return false;
}

int main()
{
	int test,times,i,j,k;
	bool over;
	scanf("%d",&times);
	for(test=1;test<=times;test++)
	{
		scanf("%d %d",&m,&n);
		for(i=0;i<m;i++)
			for(j=0;j<n;j++)
				scanf("%d",&a[i][j]);
		over=false;
		for(i=0;i<m && !over;i++)
		{
			if(chk(i))//if not all are 1
			{//cout<<"i="<<i<<endl;
				for(j=0;j<n && !over;j++)
				{
					if(a[i][j]==1)
					{//cout<<"j="<<j<<endl;
						for(k=0;k<m;k++)
						{
							if(a[k][j]!=1)
							{
								over=true;
								break;
							}
						}
					}
				}
			}
		}
		if(over)
			printf("Case #%d: NO\n",test);
		else
			printf("Case #%d: YES\n",test);
	}
	return 0;
}

