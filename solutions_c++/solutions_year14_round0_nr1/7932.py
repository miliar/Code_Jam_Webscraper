#include <stdio.h>
int main()
{
	int T;
	int caseCount=1;
	FILE *in = fopen("data.in","r");
	FILE *out = fopen("data.out","w+");
	fscanf(in,"%d",&T);
	for(caseCount=1;caseCount<=T;caseCount++)
	{
		int first,second;
		int arrange1[4][4],arrange2[4][4];
		int tmp[4];
		fscanf(in,"%d",&first);
		int i,j,k;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				fscanf(in,"%d",&arrange1[i][j]);
				if((first-1)==i)
					tmp[j]=arrange1[i][j];
			}
		int count=0,res=0;
		fscanf(in,"%d",&second);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				fscanf(in,"%d",&arrange2[i][j]);
				if((second-1)==i)
				{
					for(k=0;k<4;k++)
					{
						if(tmp[k]==arrange2[i][j])
						{	res=arrange2[i][j];count++;}
					}
				}
			}
		
		if(count==0)
			fprintf(out,"Case #%d: Volunteer cheated!\n",caseCount);
		else if(count==1)
			fprintf(out,"Case #%d: %d\n",caseCount,res);
		else
			fprintf(out,"Case #%d: Bad magician!\n",caseCount);
	}
	return 0;
}