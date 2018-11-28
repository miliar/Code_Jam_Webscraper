#include<bits/stdc++.h>
using namespace std;
int a[30];
int main()
{
	int t;
	scanf("%d",&t);
	int i,j,k;
	for(int tno=1;tno<=t;tno++)
	{
		int n;
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",a+i);
		printf("Case #%d: ",tno );
		while(1)
		{
			int f=0;
			for(i=0;i<n;i++)
			{
				if(a[i]>0)
				{
					break;
				}
			}
			if(i==n)
				break;
			for(i=0;i<n;i++)
			{
				f=0;
				if(a[i]>0)
				{
					a[i]--;
					int sum=0;
					for(j=0;j<n;j++)
					{
						sum+=a[j];
					}
					for(j=0;j<n;j++)
					{
						if(a[j]>sum/2)
							break;
					}
					if(j==n)
					{
						printf("%c ",i+'A' );
						f=1;
						break;
					}
					else
					{
						for(j=0;j<n;j++)
						{
							if(i!=j)
							{
								a[j]--;
								int sum=0;
								for(k=0;k<n;k++)
								{
									sum+=a[k];
								}
								for(k=0;k<n;k++)
								{
									if(a[k]>sum/2)
										break;
								}
								if(k==n)
								{
									printf("%c%c ",i+'A',j+'A');
									f=1;
									break;
								}
								else
								{
									a[j]++;
								}
							}
						}
						if(f==0)
						{
							a[i]++;
						}
					}
				}
			}
		}
		printf("\n");
	}
	return 0;
}