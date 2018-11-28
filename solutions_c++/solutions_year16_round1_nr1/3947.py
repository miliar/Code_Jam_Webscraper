#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t,i,j,k;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		char a[10000];
		scanf("%s",a);
		char ans[10000];
		int l = strlen(a);
		for(j=0;j<l;j++)
		{
			if(j==0)
				ans[j]=a[j];
			else
			{
				if(ans[0]>a[j])
					ans[j]=a[j];
				else
				{
					int l2 = strlen(ans);
					//printf("%s %d\n",ans,l2);
					for(k=l2-1;k>=0;k--)
					{
						//printf("%c %c\n",ans[k+1],ans[k]);
						ans[k+1]=ans[k];
					}
					ans[0] = a[j];
				}
			}
		}
		
		printf("Case #%d: %s\n",i+1,ans);
		memset(ans,0,10000);
		memset(a,0,10000);
	}
}