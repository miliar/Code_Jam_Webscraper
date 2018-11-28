#include<cstdio>
using namespace std;
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int a[4][4],x[4],y[4];
		int p,q;
		scanf("%d",&p);
		p--;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				scanf("%d",&a[j][k]);
		for(int j=0;j<4;j++)
			x[j]=a[p][j];
		scanf("%d",&q);
		q--;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				scanf("%d",&a[j][k]);
		for(int j=0;j<4;j++)
			y[j]=a[q][j];
		int ans=0;
		int num=0;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(x[j]==y[k])
				{
					ans++;
					num=x[j];
				}
			}
		}
		printf("Case #%d: ",t);
		if(ans==0)
			printf("Volunteer cheated!\n");
		else if(ans==1)
			printf("%d\n",num);
		else 
			printf("Bad magician!\n");
	}
	return 0;
}
