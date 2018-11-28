#include <iostream>
#include <stdio.h>
using namespace std;
int A[4][4];
int B[4][4];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
	int t,r1,r2,cnt=0,ans,k=0;
	scanf("%d",&t);
	while(t--)
	{
		k++;
		cnt=0;
		scanf("%d",&r1);
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		scanf("%d",&A[i][j]);

		scanf("%d",&r2);
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		scanf("%d",&B[i][j]);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(A[r1-1][i]==B[r2-1][j])
				{
					cnt++;
					if(cnt==1)
					ans=A[r1-1][i];
				}

			}
		}
		printf("Case #%d: ",k);
		if(cnt==1)
		printf("%d\n",ans);
		else
		{
			if(cnt==0)
			printf("Volunteer cheated!\n");
			else
			if(cnt>1)
			printf("Bad magician!\n");
		}

	}
	fclose(stdin);
    fclose(stdout);
	return 0;
}
