#include <stdio.h>

void onejudgement(FILE* finput,FILE* foutput,int numofcases)
{
	int thefirstrownum;
	fscanf(finput,"%d",&thefirstrownum);
	int uselessnum1;
	for (int i=0;i<(thefirstrownum-1)*4;++i)
	{
		fscanf(finput,"%d",&uselessnum1);
	}
	int firstrow[4];
	for (int i=0;i<4;++i)
	{
		fscanf(finput,"%d",&(firstrow[i]));
	}
	for (int i=0;i<(4-thefirstrownum)*4;++i)
	{
		fscanf(finput,"%d",&uselessnum1);
	}


	int thesecondrownum;
	fscanf(finput,"%d",&thesecondrownum);
	int uselessnum2;
	for (int i=0;i<(thesecondrownum-1)*4;++i)
	{
		fscanf(finput,"%d",&uselessnum2);
	}
	int secondrow[4];
	for (int i=0;i<4;++i)
	{
		fscanf(finput,"%d",&(secondrow[i]));
	}
	for (int i=0;i<(4-thesecondrownum)*4;++i)
	{
		fscanf(finput,"%d",&uselessnum2);
	}


	int thenum;
	int countofthenum=0;
	for (int i=0;i<4;++i)
	{
		for(int j=0;j<4;++j)
		{
			if (firstrow[i]==secondrow[j])
			{
				thenum=firstrow[i];
				++countofthenum;
				break;
			}
		}
	}


	switch (countofthenum)
	{
	case 0:
		fprintf(foutput,"Case #%d: Volunteer cheated!\n",numofcases+1);
		break;
	case 1:
		fprintf(foutput,"Case #%d: %d\n",numofcases+1,thenum);
		break;
	default:
		fprintf(foutput,"Case #%d: Bad magician!\n",numofcases+1);
	}



}


void main()
{
	int numofcases;
	FILE* finput;
	FILE* foutput;
	finput=fopen("A-small-attempt0.in","r");
	foutput=fopen("A-small-attempt0output.txt","w");

	fscanf(finput,"%d",&numofcases);

	for (int i=0;i<numofcases;++i)
	{
		onejudgement(finput,foutput,i);

	}

	fclose(finput);
	fclose(foutput);
}