#include <cstdio>

using namespace std;

int main()
{
	FILE *fp;
	fp=fopen("C:/Users/prabhusa/Desktop/ans.txt", "w");
	int T;
	scanf("%d",&T);
	for (int test=1;test<=T;test++) {
		int row,rownum[4],temp[4],rown[4],ans;
		scanf("%d",&row);
		for(int i=1;i<5;i++)
		{
			for(int j=0;j<4;j++)
			scanf("%d",&temp[j]);
			if(i==row)
			{	rownum[0]=temp[0];rownum[1]=temp[1];rownum[2]=temp[2];rownum[3]=temp[3]; }
			
		}		
		scanf("%d",&row);
		for(int i=1;i<5;i++)
		{
			scanf("%d%d%d%d",&temp[0],&temp[1],&temp[2],&temp[3]);
			if(i==row)
			{	rown[0]=temp[0];rown[1]=temp[1];rown[2]=temp[2];rown[3]=temp[3]; }
			
		}	
		row=0;
		for(int i=1;i<5;i++)
			for(int j=1;j<5;j++)
				if(rown[i-1]==rownum[j-1])
				{	row++;	ans=rown[i-1];}
		if(row==0)
			fprintf(fp,"Case #%d: Volunteer cheated!\n",test);
		else if(row==1)
			fprintf(fp,"Case #%d: %d\n",test,ans);
		else
			fprintf(fp,"Case #%d: Bad magician!\n",test);
	}
	return 0;
}
