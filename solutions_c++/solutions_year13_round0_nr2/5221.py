# include <fstream>
# include <iostream>
#include <vector>

using namespace std;

int **lawn;
fstream fpIn,fpOut;

void checkPattern(int lawnRows,int lawnCols)
{
	int rMax = -1,cMax=-1;
	vector<int> rowMax(lawnRows),colMax(lawnCols);

	//compute for rowsmax
	for(int i=0;i<lawnRows;i++)
	{
		rMax = lawn[i][0];
		for(int j=0;j<lawnCols;j++)
		{
			if(lawn[i][j] > rMax)
				rMax = lawn[i][j];
		}
		rowMax[i] = rMax;
	}

    //compute for colsmax
	for(int i=0;i<lawnCols;i++)
	{
		cMax = lawn[0][i];
		for(int j=0;j<lawnRows;j++)
		{
			if(lawn[j][i] > cMax)
				cMax = lawn[j][i];
		}
		colMax[i]= cMax;
	}

	//check
	for(int i=0;i<lawnRows;i++)
	{
		for(int j=0;j<lawnCols;j++)
		{
			if( (lawn[i][j] != rowMax[i]) && (lawn[i][j] != colMax[j]) )
			{
				fpOut<<"NO";
				return;
			}
		}
	}
	fpOut<<"YES";

}



void readFile()
{
    int numOfTestCases;
	int lawnRows=0,lawnCols=0;

	fpIn.open("C:\\Users\\pmalik\\Desktop\\B-large.in",ios::in);
	fpOut.open("C:\\Users\\pmalik\\Desktop\\lawnMoverOutput.txt", ios::out);

	fpIn>>numOfTestCases;

	for(int t=1;t<=numOfTestCases;t++)
	{
		fpIn>>lawnRows>>lawnCols;

		//allocate lawn 2d array
        lawn = new int*[lawnRows];
		for(int i=0;i<lawnRows;i++)
		     lawn[i] = new int[lawnCols];

		//read lawn input
		for(int i=0;i<lawnRows;i++)
		{
			for(int j=0;j<lawnCols;j++)
			{
				fpIn>>lawn[i][j];
			}
		}
		
		
		
		fpOut<<"Case #"<<t<<": ";
		checkPattern(lawnRows,lawnCols);
		if(t!=numOfTestCases)
		    fpOut<<"\n";

	
	}
    
	//close files
	fpIn.close();
	fpOut.close();
}


int main()
{
	readFile();

	char ch;
	cin>>ch;
	return 0;
}