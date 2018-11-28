#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
using namespace std;

bool isPossible( int n, int m, int ** lawn)
{
	// check each square by checking its intersecting row and column
	
	for (int i=0; i<n; ++i)
	{
		//cout << endl;
		for (int j=0; j<m; ++j)
		{
			int h = lawn[i][j];

			//cout << "checking height for square " << i << ", " << j << " :" << h << endl;

			// check the row
			bool ok = true;
			for (int k=0; k<m; ++k)
			{
				//cout << "lawn["<<i<<"]["<<k<<"]: " << lawn[i][k] << endl;
				if (lawn[i][k] > h)
				{
					ok = false;
					//cout << "break" << endl;
					break;
				}

			}

			if (ok==true)
			{
				//cout << "ok" << endl;
				continue;
			}
			// reset the value
			ok = true;
			// check the column
			//cout << "check column" << endl;
			for (int k=0; k<n; ++k)
			{
				//cout << "lawn["<<k<<"]["<<j<<"]: " << lawn[k][j] << endl;
				if (lawn[k][j] > h)
				{
					ok = false;
					break;
				}
			}

			if (ok==true)
				continue;

			// found a bad square
			return false;			

		}
	}

	// all squares good
	return true;
}

int main( int argc, const char* argv[] )
{
	ifstream myFile(argv[1]);
	int numLawns = 0;

	if (myFile.is_open())
	{
		string line;
		getline (myFile, line);
   		stringstream convert(line);
   		convert >> numLawns;

   		for (int i=0; i<numLawns; ++i)
   		{
   			getline(myFile, line);
   			int n = 0;
   			int m = 0;

   		 	convert.clear();
   		 	convert.str(line);
   		 	convert >> n;
   		 	convert >> m;

   		 	//cout << "n: " << n << ", m: " << m << endl;

   		 	int ** mylawn;
   		 	mylawn = new int*[n];
   		 	for(int j=0; j<n; ++j)
   		 		mylawn[j] = new int[m];

   		 	for(int j=0; j<n; ++j)
   		 	{
   		 		getline(myFile, line);

   		 		convert.clear();
   		 		convert.str(line);

   		 		for(int k=0; k<m; ++k)
   		 		{
   		 			convert >> mylawn[j][k];
   		 			//cout << mylawn[j][k]; 			
   		 		}
   		 		//cout << endl;
   		 	}

   		 	cout << "Case #" << (i+1) << ": ";
   		 	if (isPossible(n,m,mylawn))
   		 		cout << "YES" << endl;
   		 	else
   		 		cout << "NO" << endl;

   		 	for(int j=0; j<n; ++j)
   		 		delete [] mylawn[j];

   		 	delete [] mylawn;


   		}
	}
	return 0;
}