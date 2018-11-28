#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int t,m,n,i,j,r=1;
	int a[100][100];
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++)
		for(j=0;j<m;j++)
		scanf("%d",&a[i][j]);
		
		bool flag1=false,flag2=false,flag=false;
		
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				flag1=false,flag2=false;
				if(a[i][j]<2)
				{
					for(int k=1;k<m;k++)
					{
						if(a[i][k]!=a[i][k-1])
						{
							flag1=true;
							break;
						}
					}
					
					for(int k=1;k<n;k++)
					{
						if(a[k][j]!=a[k-1][j])
						{
							flag2=true;
							break;
						}
					}
					
					if(flag1 && flag2)
					{
						
						flag=true;
					}
					
				}
					
			}
		}
	
	if(!flag)
	{
		printf("Case #%d: YES\n",r);
	}
	else
	{
		printf("Case #%d: NO\n",r);
	}
	r++;	
		
			
	}
	return 0;
}