#include<stdio.h>
#include<string.h>

using namespace std;

int T,i,j,k,z;
int a[2][5][5],b[2],c[2];

int main() {

	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	
	scanf("%d",&T);
	
	for(z=1;z<=T;z++)
	{
		for(k=0;k<2;k++)
		{
			scanf("%d",&b[k]);
			for(i=0;i<4;i++)
				for(j=0;j<4;j++)
					scanf("%d",&a[k][i][j]);
			c[k]=0; i=b[k]-1;
			for(j=0;j<4;j++)
				c[k]|=(1<<a[k][i][j]);
		}
		k=c[0]&c[1];
		printf("Case #%d: ",z);
		if(k==0)
		{
			puts("Volunteer cheated!");
		}
		else if(k!=(k&-k))
		{
			puts("Bad magician!");
		}
		else
		{
			for(i=1;i<=16;i++)
				if((k^(1<<i))==0)
					printf("%d\n",i);
		}
	}
	
	return 0;

}
