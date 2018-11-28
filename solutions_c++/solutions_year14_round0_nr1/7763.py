#include<cstdio>
using namespace std;
int main()
{
	int t,a[4][4],i,j,k,st[2][17]={0},c=0,ans,ca=0,m;
	scanf("%d",&t);
	while(t--)
	{
		ca++;
		c = 0;
		for (i=1;i<=16;i++)
			st[0][i] = st[1][i] = 0;
		for (m=0;m<2;m++)
		{
			scanf("%d",&k);
			for (i=0;i<4;i++)
				for (j=0;j<4;j++)
					scanf("%d",&a[i][j]);
			for (i=0;i<4;i++)
				st[m][a[k-1][i]] = 1;
		}
		for (i=1;i<=16;i++)
			if (st[0][i]==1 && st[1][i]==1)
			{
				c++;
				ans = i;
			}
		if (c==0)
			printf("Case #%d: Volunteer cheated!\n",ca);
		else if (c > 1)
			printf("Case #%d: Bad magician!\n",ca);
		else
			printf("Case #%d: %d\n",ca,ans);

	}

	return 0;
}
