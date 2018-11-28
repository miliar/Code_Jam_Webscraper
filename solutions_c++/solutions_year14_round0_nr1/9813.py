#include <cstdio>

using namespace std;

int main()
{
	int c,cases;
	int r;
	int matrix[4][4];
	int possible[4];
	int count;
	int last;

	c=0;
	for(scanf("%d",&cases);c<cases;c++)
	{
		scanf("%d",&r);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&(matrix[i][j]));
		for(int i=0;i<4;i++)
			possible[i] = matrix[r-1][i];

		scanf("%d",&r);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&(matrix[i][j]));

		count = 0;
		last = -1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(possible[i] == matrix[r-1][j])
				{
					count++;
					last = matrix[r-1][j];
				}

		printf("Case #%d: ",c+1);
		if(count == 1)
			printf("%d\n",last);
		else if(count > 1)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
	}

	return 0;
}
