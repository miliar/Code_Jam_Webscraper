#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

void main(void)
{
	int n=0, y1, y2;
	int a[4][4], b[4][4];
	int x[4], z[4];
	int sovp, numofsovp=0;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	scanf("%i",&n);
	for(int k=1; k<=n;k++)
	{
		scanf("%i",&y1);
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf("%i",&a[i][j]);
		for(int i=0;i<4;i++)
			x[i]=a[y1-1][i];
		scanf("%i",&y2);
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf("%i",&b[i][j]);
		for(int i=0;i<4;i++)
			z[i]=b[y2-1][i];
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				if(x[i]==z[j])
				{
					numofsovp++;
					sovp=x[i];
				}
			}
		if(numofsovp==1)
			printf("Case #%i: %i\n", k, sovp);
		if(numofsovp>1) 
			printf("Case #%i: Bad magician!\n", k);
		if(numofsovp==0)
			printf("Case #%i: Volunteer cheated!\n", k);
		numofsovp=0;
	}
}
