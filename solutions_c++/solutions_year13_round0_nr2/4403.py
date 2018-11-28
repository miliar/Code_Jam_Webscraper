#include <stdio.h>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	int a[100][100];
	for (int i1= 1; i1 <= t; ++i1)
	{
		int n,m;
		scanf("%d %d",&n,&m);
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
				scanf("%d",&a[i][j]);
				
		}
		int i;
		for (i = 0; i < n; ++i)
		{
			int j;
			for (j = 0; j < m; ++j)
			{
				bool flag =true; 
				for (int k = 0; k < m; ++k)
				{
					if(a[i][k]>a[i][j])
					{
						flag=false;
						break;
					}
				}
				if(flag==false)
				{
					flag =true; 
					for (int k = 0; k < n; ++k)
					{
						if(a[k][j]>a[i][j])
						{
							flag=false;
							break;
						}
					}
				}
				if(flag==false)
				{
					printf("Case #%d: NO\n",i1);
					break;
				}
			}
			if(j<m)
			break;
		}
		if(i==n)
			printf("Case #%d: YES\n",i1);
	}

}