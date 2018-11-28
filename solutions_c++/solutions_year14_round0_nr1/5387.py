#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int a[4][4],b[4][4];

int main()
{
	int t,ys;

	freopen("A-small-attempt0.in","r",stdin);
	freopen("Ares.out","w",stdout);

	ys=0;
	scanf("%d",&t);
	while (t--)
	{
		int la,lb;
		scanf("%d",&la);
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&lb);
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
				scanf("%d",&b[i][j]);
		la--; lb--;
		int cnt=0;
		int ans;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
				if (a[la][i]==b[lb][j])
				{
					cnt++;
					ans=a[la][i];
				}

		printf("Case #%d: ",++ys);

		if (cnt==1)
			printf("%d\n",ans);
		else if (cnt==0)
			printf("Volunteer cheated!\n");
		else
			printf("Bad magician!\n");
	}

	return 0;
}


