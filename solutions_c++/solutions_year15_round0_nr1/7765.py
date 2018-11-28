#include <fstream>
#include <iostream>

using namespace std;

int main ()
{
		ifstream		inputFile;			// variable to store input file
		ofstream		outputFile;		// variable to store output file	
		int				testcase;

		//program specific variables
		int				sMax;
		int				ans;
		char			temp[2] = "1";
		int				total;

	//open the files
	inputFile.open  ("A-large.in", ios::in);
	outputFile.open ("A-large.out", ios::out);

	//read the number of test cases
	inputFile>>testcase;
	//execute the test cases
	for (int testIterator = 0; testIterator < testcase; testIterator++){

		//the test case execution block
		{
			inputFile>>sMax;
			ans = 0;
			total = 0;

			if (sMax == 0){
				outputFile<<"Case #"<<testIterator+1<<": "<<ans<<"\n";

				char * c= (char*) malloc (sizeof(char)*(sMax+2));

				inputFile>>c;

				free (c);
				continue;
			}

			char * c= (char*) malloc (sizeof(char)*(sMax+2));

			inputFile>>c;

			temp[0]=c[0];
			
			if(atoi(temp))
				total = atoi(temp);
			else
				total = ans = 1;

			for (int iterator = 1; iterator <= sMax; iterator ++)
			{
				temp[0] = c[iterator];
				if (!atoi(temp) && total <= iterator){
					total++;
					ans++;
				} else {
					total += atoi(temp);
				}

			}
						
			c[sMax] = '\0';
			free (c);

			outputFile<<"Case #"<<testIterator+1<<": "<<ans<<"\n";
		}
	}

	//close the files
	inputFile.close  ();
	outputFile.close ();

	return 0;
}