#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char* argv[] )
{
	ifstream inFile;
	ofstream outFile;

	string outputFilename = "out.txt";
	inFile.open(argv[1], ios::in);
	outFile.open(outputFilename, ios::out);

	char output[100];
	if(!inFile.is_open())
	{
		cout<<"Invalid input file!"<<endl;
		return -1;
	}

	//Begin calculations
	//First line is number of test cases
	inFile>>output;
	int T = atoi(output);
	
	// while(!inFile.eof())
	// {
	// 	inFile>>output;
	// 	cout<<output<<endl;;
	// 	cout<<"iteration: "<<i++<<endl;;
	// }

	int arr1[4][4];
	int arr2[4][4];

	// Run for T test cases
	for(int i=0; i < T; i++)
	{

		inFile >> output;
		int rowGuess1 = atoi(output);
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				inFile >> output;
				arr1[j][k] = atoi(output);
			}
		}

		inFile >> output;
		int rowGuess2 = atoi(output);
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				inFile >> output;
				arr2[j][k] = atoi(output);
			}
		}

		int res1[4];
		int res2[4];


		for(int itr = 0; itr < 4; itr++)
		{
			res1[itr] = arr1[rowGuess1-1][itr];
		}


		for(int itr = 0; itr < 4; itr++)
		{
			res2[itr] = arr2[rowGuess2-1][itr];
		}

		int matches = 0;
		int firstMatch = -1;
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				if (res1[j] == res2[k])
				{
					if(firstMatch == -1)
					{
						firstMatch = res1[j];
						
					}
					matches++;
				}
			}
		}
		

		if(matches == 1)
		{
			outFile<<"Case #"<<i+1<<": "<<firstMatch<<endl; 
		}
		else if(matches > 1)
		{
			outFile<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
		}
		else
		{
			outFile<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
		}


	 }


	// while(!inFile.eof())
	// {
	// 	inFile>> output;
	// 	cout<<output;
	// }
	
	inFile.close();

	//Writing output to a file
	

	outFile.close();
	return 0;
}