#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tc;
	scanf("%d",&tc);
	int arr[17];int c=1;
	while(tc--)
	{
		for(int i=0;i<17;i++)
			arr[i]=0;
		int idx;
		for(int k=0;k<2;k++)
		{
			scanf("%d",&idx);
			for(int i=1;i<=4;i++)
				for(int j=1;j<=4;j++)
				{
					int x;
					scanf("%d",&x);
					if(i==idx)arr[x]++;
				}
		}
		int res=-1;
		for(int i=1;i<17;i++)
			if(arr[i]==2)
			{
				if(res==-1)
				res=i;
				else res=-2;
			}
		if(res>0)
		printf("Case #%d: %d\n",c,res);
		else if(res==-1)
		{
			printf("Case #%d: Volunteer cheated!\n",c);
		}
		else printf("Case #%d: Bad magician!\n",c);
		c++;
	}
	return 0;
}
