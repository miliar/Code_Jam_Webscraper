#include <iostream>
#include <fstream>


using namespace std;


bool testPattern(int **lawn, int rows, int cols)
{
	int * max_rows = new int [rows];
	int * max_cols = new int [cols];
	

	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			
			if (max_cols[j] < lawn[i][j])
				max_cols[j] = lawn[i][j];
			if (max_rows[i] < lawn[i][j])
				max_rows[i] = lawn[i][j];
		}
	}
	
//	for (int i = 0; i < rows; i++)
//		cout << max_rows[i] << " ";
//	cout << endl;

//	for (int j = 0; j < cols; j++)
//		cout << max_cols[j] << " ";

	

	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			if ((lawn[i][j] < max_cols[j]) && (lawn[i][j] < max_rows[i]))
			{
				return false;
				
			}
		}	
	}

	return true;

}

void runTest(ifstream& file, string & outputString)
{
	outputString = "Test";
	
	int rows, cols;
	
	file >> rows >> cols;
	
	
	int **lawn = new int* [rows];
	
	for ( int i =0 ; i< rows; i++)
	{
		lawn[i] = new int [cols];
		for( int j=0; j < cols; j++)
		{
			file >> lawn [i][j] ;
			//cout << lawn[i][j] << " ";
		}
		//cout << endl;
	}

	
	bool result = testPattern(lawn, rows, cols);
	if (result)
		outputString = "YES";
	else
		outputString = "NO";

}


int main(int argc, char* argv[])
{

	
	ifstream inFile;
	ofstream outFile;
	
	inFile.open(argv[1]);
	
	outFile.open(argv[2]);

	int numTests;
	inFile >> numTests;
	
	// other variables
	
	
	for (int i = 0; i < numTests; i++)
	{
		string outputString;
		//cout << endl << "CASE " << i+1 << endl;
		runTest(inFile, outputString);
		outFile << "Case #" << i+1 << ": " << outputString << endl;
	}

	
	inFile.close();
	outFile.close();


}
