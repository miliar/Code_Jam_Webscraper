#include <stdio.h>
#include <algorithm>

using namespace std;
int temp[4][4];
int t2[4];
int t3[4];
int c;
int f;
int main()
{
	int t;
	int row;
	freopen("d:\\A-small-attempt6.in","r",stdin);
	freopen("d:\\output6.out","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{

		scanf("%d",&row);
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				scanf("%d",&temp[j][k]);
			}
		}
		for(int j=0;j<4;j++){t2[j]=temp[row-1][j];}
		

		scanf("%d",&row);
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				scanf("%d",&temp[j][k]);
			}
		}
		for(int j=0;j<4;j++){t3[j]=temp[row-1][j];}
		sort(t2,t2+4);
		sort(t3,t3+4);

		int idx1=0,idx2=0;
		c=0;
		while(idx1<4&&idx2<4)
		{
			if(t2[idx1]==t3[idx2])
			{
				c++;
				f=t2[idx1];
				idx1++;
				idx2++;
				if(c>1){break;}
			}
			else if(t2[idx1]>t3[idx2])
			{
				idx2++;
			}else
			{
				idx1++;
			}
		}

		if(c==0)
		{
			printf("Case #%d: ",i);
			printf("Volunteer cheated!\n");
		}else if(c==1)
		{
			printf("Case #%d: ",i);
			printf("%d\n",f);
		}else
		{
				printf("Case #%d: ",i);
				printf("Bad magician!\n");
		}
		
	}

	//system("pause");
	return 0;
}