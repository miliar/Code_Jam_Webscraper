#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		bool canbedone=true;
		int n,m;
		scanf("%d",&n);
		scanf("%d",&m);
		int a[n][m];
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<m;k++)
			scanf("%d",&a[j][k]);
		}
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<m;k++)
			{
				bool rows=true,columns=true;
				for(int l=0;l<n;l++)
				{
					if(a[l][k]>a[j][k])
					{
						columns=false;
						break;
					}
				}
				for(int l=0;l<m;l++)
				{
					if(a[j][l]>a[j][k])
					{
						rows=false;
						break;
					}
				}
				if(!rows && !columns)
				{
					canbedone=false;
					break;
				}
			}
			if(!canbedone)
			break;
		}
		if(canbedone)
		printf("Case #%d: YES\n",i);
		else
		printf("Case #%d: NO\n",i);
	}
}
