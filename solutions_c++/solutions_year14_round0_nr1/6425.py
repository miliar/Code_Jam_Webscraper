#include <cstdio>

using namespace std;

int main(int argc, char const *argv[])
{
	int t, c, pos, caseNum=1;
	int arr1[4][4], arr2[4][4], m, n;
	scanf("%d",&t);
	while(t--)
	{
		c=0;
		scanf("%d",&m);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d", &arr1[i][j]);

		scanf("%d",&n);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d", &arr2[i][j]);
		
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(arr1[m-1][i] == arr2[n-1][j])
				{
					pos = arr1[m-1][i];
					c++;
				}
			}
		}

		if(c==1)
		{
			printf("Case #%d: %d\n", caseNum++, pos);
		}
		else if(c==0)
		{
			printf("Case #%d: Volunteer cheated!\n", caseNum++);
		}
		else
		{
			printf("Case #%d: Bad magician!\n", caseNum++);
		}
	}
	return 0;
}