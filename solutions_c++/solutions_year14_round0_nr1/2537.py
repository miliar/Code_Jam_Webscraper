#include <iostream>
using namespace std;

int main()
{
	FILE* fp = fopen("D:\\workspace\\codejam\\A-small-attempt0.in","r");
	FILE* fo = fopen("D:\\workspace\\codejam\\result.txt","w");

	int tSize, fAns, sAns;
	int fCards[4][4], sCards[4][4];
	fscanf(fp,"%d\n",&tSize);

	for (int i = 1; i<=tSize; i++)
	{
		fscanf(fp,"%d\n",&fAns);
		for (int ii = 0; ii<4; ii++)
		{
			for (int jj = 0; jj<3; jj++)
				fscanf(fp,"%d ",&fCards[ii][jj]);
			fscanf(fp,"%d\n",&fCards[ii][3]);
		}

		fscanf(fp,"%d\n",&sAns);
		for (int ii = 0; ii<4; ii++)
		{
			for (int jj = 0; jj<3; jj++)
				fscanf(fp,"%d ",&sCards[ii][jj]);
			fscanf(fp,"%d\n",&sCards[ii][3]);
		}

		int ansCount = 0;
		int ans = 0;
		for (int ii = 0; ii<4;ii++)
		{
			for (int jj = 0; jj<4; jj++)
			{
				if (fCards[fAns-1][ii] == sCards[sAns-1][jj])
				{
					ansCount++;
					ans = fCards[fAns-1][ii];
				}
			}
		}

		fprintf(fo,"Case #%d: ",i);
		if (ansCount == 0)
			fprintf(fo,"Volunteer cheated!\n");
		else if (ansCount>1)
			fprintf(fo,"Bad magician!\n");
		else
			fprintf(fo,"%d\n",ans);
	}

	fclose(fp);

	return 0;
}