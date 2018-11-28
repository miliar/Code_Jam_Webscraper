#include "stdio.h"
#include "stdlib.h"

int match(int *row1, int *row2)
{
	int count=0, nos;

	// for (int i = 0; i < 4; ++i) printf("%d ",row1[i] );
	// 	printf("\n");
	// for (int i = 0; i < 4; ++i) printf("%d ",row2[i] );
	
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if(row1[i]==row2[j])
			{
				count++;
				//printf("%d ",row2[j] );
				nos = row2[j];	
			} 
		}
	}
	if(count==0) return 0;
	if(count>1) return -1;
	return nos;
}

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d",&t);
	for (int cas = 1; cas <= t; ++cas)
	{
		printf("Case #%d: ",cas );
		int r1,r2, a1[4][4],a2[4][4];
		scanf("%d",&r1);
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				scanf("%d",&(a1[i][j]));
			}
		}
		scanf("%d",&r2);
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				scanf("%d",&(a2[i][j]));
			}
		}
		//printf("%d %d ",r1,r2 );
		int m=match(a1[r1-1],a2[r2-1]);
		if(m==0) printf("Volunteer cheated!\n");
		else if(m==-1) printf("Bad magician!\n");
		else printf("%d\n",m ); 
	}
}