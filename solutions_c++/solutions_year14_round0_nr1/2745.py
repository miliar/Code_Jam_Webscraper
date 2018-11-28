#include<stdio.h>

int main()
{
	int T;
	int A[5][5];
	int i,j,k,B[5],C[5],sum;
	int b,c,D[5];
	scanf("%d",&T);
	for(k=1;k<=T;k++)
	{
		sum = 0;
		scanf("%d",&b);
		b--;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		scanf("%d",&A[i][j]);
		for(j=0;j<4;j++)
		B[j] = A[b][j];
		
		scanf("%d",&c);
		c--;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		scanf("%d",&A[i][j]);
		for(j=0;j<4;j++)
		C[j] = A[c][j];
		
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			if(B[i]==C[j])
			D[sum]=B[i],sum++;
		}
		
		if(sum==1)
		printf("Case #%d: %d\n",k,D[0]);
		else if(sum>1)
		printf("Case #%d: Bad magician!\n",k);
		else
		printf("Case #%d: Volunteer cheated!\n",k);
		
	}
	
}
