#include <string>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main()
{
	string line;
	ifstream myReadFile;
	ofstream myfile;
	myfile.open ("output.txt");
 
	myReadFile.open("A-small-attempt2.in");
	int numberOfTest;
	myReadFile >> numberOfTest;
	for (int i = 0; i< numberOfTest; i++)
	{
		int rowFirstRep, rowSeconRep;
		int bigRow[8];
		myReadFile>>rowFirstRep;
		for (int i = 0; i<rowFirstRep; i++)
			getline(myReadFile, line);
		myReadFile>>bigRow[0]>>bigRow[1]>>bigRow[2]>>bigRow[3];
		for (int i = 0; i< 4 - rowFirstRep + 1; i++)
			getline(myReadFile,line);
				
		myReadFile>>rowSeconRep;
		for (int i = 0; i<rowSeconRep; i++)
			getline(myReadFile, line);
		myReadFile>>bigRow[4]>>bigRow[5]>>bigRow[6]>>bigRow[7];		
		for (int i = 0; i< 4 - rowSeconRep + 1; i++)
			getline(myReadFile,line);


		qsort(bigRow,8,sizeof(int),compare);
		int numberOfSimilar = 0;
		int result;
		for (int i = 0; i< 8; i++)
		{
			if (bigRow[i] == bigRow[i+1])	
			{
				numberOfSimilar++;
				result = bigRow[i];
			}
		}
		myfile<< "Case #" << i + 1 <<": ";
		if (numberOfSimilar == 0)
			myfile<<"Volunteer cheated!";
		else if (numberOfSimilar == 1)
			myfile<<result;
		else 
			myfile<<"Bad magician!";
		myfile<<endl;

	}

	myReadFile.close();  
	myfile.close();
	return 0;
}