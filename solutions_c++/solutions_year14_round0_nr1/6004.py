#include<stdio.h>
int main()
{
	int t,r,row1,row2,i,j,mat[4],mat2[4],final,check,trash=0;
	int k = 0;
	scanf("%d", &t);
	for(r=1;r<=t;r++)
	{
		scanf("%d", &row1);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(i<=row1)
					scanf("%d", &mat[j-1]);
				else
					scanf("%d",&trash);
			}
		}

		scanf("%d", &row2);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(i<=row2)
					scanf("%d", &mat2[j-1]);
				else
					scanf("%d",&trash);
			}
		}
		for(i=0;i<4;i++)
		{
			check = mat[i];	
			for(j=0;j<4;j++)
			{
				if(mat2[j] == check)
				{
					if(k == 0)
						final = check;	
					k++;
					
				}
			}
		}
		if(k == 1)
			printf("Case #%d: %d\n", r, final);

		else if(k == 0)
			printf("Case #%d: Volunteer cheated!\n", r);
		else
			printf("Case #%d: Bad magician!\n", r);
		k = 0;
	}
	return 0;
}
