#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int main()
{
	freopen("out.txt","w",stdout);
	freopen("A-small-attempt2.in","r",stdin);
	int t,ans[4],b[4],a[4],an,c;
	scanf("%d",&t);	
	for(int T=0;T<t;T++)
	{
		an=0;
		scanf("%d",&c);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)scanf("%d",&a[j]);
			if(c==i+1) for(int j=0;j<4;j++)b[j]=a[j];
		}
		scanf("%d",&c);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)scanf("%d",&a[j]);
			if(c==i+1)
			{
				for(int j=0;j<4;j++)
				{
					for(int k=0;k<4;k++)
					{
						if(a[j]==b[k])
						{
							ans[an]=a[j];
							an++;
						}
					}
					
				}
			}
		}

		printf("Case #%d: ",T+1);
		if(an==0)printf("Volunteer cheated!");
		if(an==1)printf("%d",ans[0]);
		if(an>1)printf("Bad magician!");
		printf("\n");
	}
	return 0;
}
