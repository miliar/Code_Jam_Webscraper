#include <stdio.h>

int n = 1;
FILE *in = fopen("A-small-attempt0.in", "r");
FILE *out = fopen("output.txt", "w");
void doTestCase()
{
	//first try
	int iRow;
	int iArrCardShuffle[4][4];
	fscanf(in, "%d",&iRow);
	int iArrSaveRow[4];
	int iArrSaveCol[4];
	for(int i=0; i<4; ++i)
	{

		if( i+1 == iRow)
		{

			for(int j=0; j<4; ++j)
			{
				fscanf(in, "%d",&iArrSaveRow[j]);
			}
		}
		else
		{
			int trash;
			for(int j=0; j<4; ++j)
			{
				fscanf(in, "%d",&trash);
			}
		}
	}	
	//second try
	fscanf(in, "%d",&iRow);
	for(int i=0; i<4; ++i)
	{

		if( i+1 == iRow)
		{

			for(int j=0; j<4; ++j)
			{
				fscanf(in, "%d",&iArrSaveCol[j]);
			}
		}
		else
		{
			int trash;
			for(int j=0; j<4; ++j)
			{
				fscanf(in, "%d",&trash);
			}
		}
	}	

	//valid magic
	bool checkMagic[4][4];
	int validCounter = 0;
	int saveIndex;
	for(int i=0; i<4; ++i)
	{
		 for(int j=0; j<4; ++j)
		 {
			 checkMagic[i][j] = false;
			 if(iArrSaveRow[i] == iArrSaveCol[j])
			 {
				 saveIndex = i;
				 checkMagic[i][j] = true;
				 validCounter ++;
			 }
		 }
	}
	fprintf(out, "Case #%d: ", n++);
	if( validCounter == 1)
	{//if magic valid
		fprintf(out, "%d\n", iArrSaveRow[saveIndex]);
	}
	else if( validCounter > 1)
	{
		fprintf(out, "Bad magician!\n");
	}
	else
	{
		fprintf(out, "Volunteer cheated!\n");
	}
}
int main(void)
{
	int testCase;
	fscanf(in, "%d", &testCase);

	while(testCase--)
	{
		doTestCase();
	}
	fclose(in);
	fclose(out);
}