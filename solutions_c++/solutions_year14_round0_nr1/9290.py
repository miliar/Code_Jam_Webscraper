#include <stdio.h> 

int main ()
{
	int n1,n2,m1,m2,i,j,i1,i2,k,mark;
	int a[4][4],b[4][4];
	scanf("%d",&n1);
	n2=1;
	while(n2<=n1)
	{
		scanf("%d",&i);
		scanf("%d%d%d%d",&a[0][0],&a[0][1],&a[0][2],&a[0][3]);
		scanf("%d%d%d%d",&a[1][0],&a[1][1],&a[1][2],&a[1][3]);
		scanf("%d%d%d%d",&a[2][0],&a[2][1],&a[2][2],&a[2][3]);
		scanf("%d%d%d%d",&a[3][0],&a[3][1],&a[3][2],&a[3][3]);
		scanf("%d",&j);
		scanf("%d%d%d%d",&b[0][0],&b[0][1],&b[0][2],&b[0][3]);
		scanf("%d%d%d%d",&b[1][0],&b[1][1],&b[1][2],&b[1][3]);
		scanf("%d%d%d%d",&b[2][0],&b[2][1],&b[2][2],&b[2][3]);
		scanf("%d%d%d%d",&b[3][0],&b[3][1],&b[3][2],&b[3][3]);
		mark=0;
		for(m1=0;m1<4;m1++)
		{
			for(m2=0;m2<4;m2++)
			{
				if(a[i-1][m1]==b[j-1][m2])
				{
					k=a[i-1][m1];
					mark++;
				}
			}
		}
		printf("Case #%d: ",n2);
		if(mark==1)
			printf("%d\n",k);
		else if(mark==0)
				printf("Volunteer cheated!\n");
				else
				printf("Bad magician!\n");
		n2++;
	}
	return 0;
}
