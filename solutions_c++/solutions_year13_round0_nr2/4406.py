#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,u;
	scanf("%d",&t);
	int a[105][105];
	for(u=0;u<t;u++)
	{
		int n,m;
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
				scanf("%d",&a[i][j]);
			
		}
		int flag=0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				for(int k=0;k<m;k++)
				{
					if(a[i][k]>a[i][j])
					{
						for(int o=0;o<n;o++)
						{
							if(a[o][j]>a[i][j])
							{
								flag=1;
								break;
							}
						}
						break;

					}
				}

				if(flag==1)
					break;
			}
			if(flag==1)
				break;
		}
		if(flag==1)
			printf("Case #%d: NO\n",u+1);
		else
			printf("Case #%d: YES\n",u+1);
	}
}
