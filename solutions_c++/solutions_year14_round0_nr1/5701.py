#include<cstdio>
#include<cstring>

using namespace std;

int ans[20];
int r1;
int a[5][5];

int main()
{
	int t;
	scanf("%d",&t);
	int cas = 0;
	while (t--)
	{
		scanf("%d",&r1);
		memset(ans,0,sizeof(ans));

		for (int i = 1 ; i <= 4 ; i++)
			for (int j = 1 ; j <= 4 ; j++)
				scanf("%d",&a[i][j]);
		for (int j = 1 ; j <= 4 ; j++)
			ans[a[r1][j]]++;

		scanf("%d",&r1);
		for (int i = 1 ; i <= 4 ; i++)
			for (int j = 1 ; j <= 4 ; j++)
				scanf("%d",&a[i][j]);
		for (int j = 1 ; j <= 4 ; j++)
			ans[a[r1][j]]++;

		int out;
		int cnt = 0;
		for (int i = 1 ; i <= 16 ; i++)
			if (ans[i] == 2)
			{
				out = i;
				cnt++;
			}
		printf("Case #%d: ",++cas);
		if (cnt == 0) puts("Volunteer cheated!");
		else if (cnt == 1) printf("%d\n",out);
		else puts("Bad magician!");
	}
	return 0;
}
