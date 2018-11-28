#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
using namespace std;
const int maxn=100+10;

struct nodes
{
	int row;
	int num[10][10];
}mat[5];
int ans[5];
int p=0;

int main ()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("woca.txt","w",stdout);
	int t;
	while (scanf("%d",&t)==1)
	{
		for (int ii=1;ii<=t;ii++)
		{
			p=0;
			for (int k=0;k<2;k++)
			{
				scanf("%d",&mat[k].row);
				mat[k].row--;
				for (int i=0;i<4;i++)
				{
					for (int j=0;j<4;j++)
					{
						scanf("%d",&mat[k].num[i][j]);
					}
				}
			}
			for (int i=0;i<4;i++)
			{
				for (int j=0;j<4;j++)
				{
					if (mat[0].num[mat[0].row][i]==mat[1].num[mat[1].row][j])
					{
						ans[p++]=mat[0].num[mat[0].row][i];break;
					}
				}
			}
			if (!p)
			{
				printf("Case #%d: Volunteer cheated!\n",ii);
			}
			else if (p==1)
			{
				printf("Case #%d: %d\n",ii,ans[0]);
			}
			else
			{
				printf("Case #%d: Bad magician!\n",ii);
			}
		}
	}
	fclose(stdout);
	fclose(stdin);
	return 0;
}