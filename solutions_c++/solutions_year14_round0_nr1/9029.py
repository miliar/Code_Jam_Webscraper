#include<cstdio>
using namespace std;
int main()
{
	int T,i,j,k,arr1[5][5],arr2[5][5],r1,r2,count,save;
	scanf("%d",&T);
	for(k=1;k<=T;k++)
	{
		scanf("%d",&r1);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&arr1[i][j]);
		scanf("%d",&r2);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&arr2[i][j]);
		count=0;
		save=0;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				if(arr1[r1][i]==arr2[r2][j])
				{
					count++;
					save=arr1[r1][i];
				}
		if(count==1)
			printf("Case #%d: %d\n",k,save);
		if(count==0)
			printf("Case #%d: Volunteer cheated!\n",k);
		if(count>1)	
			printf("Case #%d: Bad magician!\n",k);		
	}
	return 0;
}
