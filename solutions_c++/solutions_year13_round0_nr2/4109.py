#include <iostream.h>
#include <fstream.h>

// Code Jam 2013
// Qualification Round
// Problem B. Lawnmower


int main(int argc, char *argv[])
{
	int T;
	int t;
	
	int N;
	int n;
	int M;
	int m;
	
	int high;
	
	bool bpossible;
	
	int lawnrequirements[100][100];
	
	int lawn[100][100];
	
	ifstream inFile;
	
	//inFile.open("test.in");
	if ( argc < 2 )
	{
		cout << "No input file given!" << endl;
		exit(1);
	}
	inFile.open(argv[1]);
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> T;
	
	for (t=0;t<T;t++)
	{
		inFile >> N;
		inFile >> M;
		
		// read lawn requirements and initialize lawn
		for (n=0;n<N;n++)
		{
			for (m=0;m<M;m++)
			{
				inFile >> lawnrequirements[n][m];
				// initialize lawn
				lawn[n][m] = 100;
			}
		}
		
		// a "run" is done by mowing with the highest found number in a row/column
		
		// doing rows
		for (n=0;n<N;n++)
		{
			// find highest point
			high = 1;
			for (m=0;m<M;m++)
			{
				if ( lawnrequirements[n][m] > high )
				{
					high = lawnrequirements[n][m];
				}
			}
			
			// mow row
			for (m=0;m<M;m++)
			{
				if ( lawn[n][m] > high )
				{
					lawn[n][m] = high;
				}
			}
			
		}
		
		// doing columns
		for (m=0;m<M;m++)
		{
			// find highest point
			high = 1;
			for (n=0;n<N;n++)
			{
				if ( lawnrequirements[n][m] > high )
				{
					high = lawnrequirements[n][m];
				}
			}
			
			// mow column
			for (n=0;n<N;n++)
			{
				if ( lawn[n][m] > high )
				{
					lawn[n][m] = high;
				}
			}
			
		}
		
		bpossible = 1;
		for (n=0;n<N;n++)
		{
			for (m=0;m<M;m++)
			{
				if ( lawn[n][m] != lawnrequirements[n][m] )
				{
					bpossible = 0;
				}
			}
		}
		
		if  (bpossible)
		{
			cout << "Case #" << t+1 << ": YES" << endl;
		}
		else
		{
			cout << "Case #" << t+1 << ": NO" << endl;
		}
	}
		
		
	
	inFile.close();
	return 0;
}