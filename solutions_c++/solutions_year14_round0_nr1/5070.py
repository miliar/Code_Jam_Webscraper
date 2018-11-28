#include<stdio.h>
using namespace std;
int a[4][4],b[4][4];
int main()
{
	int k,i,j,t,c,z,n,m;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		c=0;
		z=0;
		scanf("%d",&n);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&m);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&b[i][j]);
		for(i=0;i<4;i++)
			{
			for(j=0;j<4;j++)
			{
				if(a[n-1][i]==b[m-1][j]) {++c; z=i;}
			}
			}
		printf("Case #%d: ",k);
		if(c==1) printf("%d\n",a[n-1][z]);
		else if(c>1) printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
	return 0;
}