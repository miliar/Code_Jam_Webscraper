#include <stdio.h>



int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	int T;
	scanf("%d",&T);
	int row1, row2;
	int mat1[4][4] , mat2[4][4];
	int Cas = 1;
	while (T-- >0)
	{
		//read row1
		scanf("%d",&row1);
		for (int i=0; i<4;i++)
			scanf("%d %d %d %d",&mat1[i][0],&mat1[i][1],&mat1[i][2],&mat1[i][3]);
		
		//read row2
		scanf("%d",&row2);
		for (int i=0; i<4;i++)
			scanf("%d %d %d %d",&mat2[i][0],&mat2[i][1],&mat2[i][2],&mat2[i][3]);
		
		bool exist=false, isDoubled=false;
		int guess;

		for ( int i = 0; i<4; i++)
		{
			for (int j=0;j<4;j++)
			{
				if (mat1[row1-1][i]==mat2[row2-1][j])
				{
					if (exist)
					{
						isDoubled = true;
						break;

					}else
					{
						exist=true;
					}
					guess = mat1[row1-1][i];
				}
				if (isDoubled)
					break;
				
			}
		}
		if (isDoubled)
			printf("Case  #%d: Bad magician!\n",Cas);
		else if (exist)
			printf("Case  #%d: %d\n",Cas,guess);
		else
			printf("Case  #%d: Volunteer cheated!\n",Cas);
		
		Cas++;
	}
	return 0;
}