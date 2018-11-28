#include<iostream>
using namespace std;
int matrix1[5][5],matrix2[5][5];
int first,second;
int count[17];
int main()
{
	freopen("..\\Debug\\A-small-attempt0.in","r",stdin);
	freopen("..\\Debug\\A-small-attempt0.out","w",stdout);
	int t,i,j,m,number,index;
	scanf("%d",&t);
	m=1;
	while (m<=t)
	{
		number=0;
		memset(count,0,sizeof(count));
		scanf("%d",&first);
		for (i=1;i<=4;i++)
		{
			for (j=1;j<=4;j++)
			{
				scanf("%d",&matrix1[i][j]);
				if (i==first)
				{
					count[matrix1[i][j]]++;
				}
			}
		}
		scanf("%d",&second);
		for (i=1;i<=4;i++)
		{
			for (j=1;j<=4;j++)
			{
				scanf("%d",&matrix2[i][j]);
				if (i==second)
				{
					count[matrix2[i][j]]++;
				}
			}
		}

		for (i=1;i<=4;i++)
		{
			if (count[matrix1[first][i]]==2)
			{
				number++;
				index=i;
			}
		}
		if (number>=2)
		{
			printf("Case #%d: Bad magician!\n",m);
		}
		else if (number==0)
		{
			printf("Case #%d: Volunteer cheated!\n",m);
		}
		else
		{
			printf("Case #%d: %d\n",m,matrix1[first][index]);
		}
		m++;
	}
	cin>>i;
	return 0;
}