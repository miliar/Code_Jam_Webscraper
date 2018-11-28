/*template for gcj*/

#include <iostream>
#include <fstream>
#include <vector>
#include <iterator>
#include <string>

using namespace std;

unsigned long And(unsigned long, unsigned long);

int main(){

	ifstream inFile;
	const char *fileName = "B-small-attempt0.in";//input file name;
	inFile.open(fileName);
	ofstream outFile("gcj_900am_output.txt");//answer file name
	int caseNumber;
	// unsigned long numA;
	// unsigned long numB;
	// unsigned long numK;
	// unsigned long tempResult;
	long numA;
	long numB;
	long numK;
	long tempResult;
	long count = 0;

	std::vector<unsigned long> allPairs;


	if (inFile.is_open()){
		inFile >> caseNumber;
		//data input
		cout << "case number: " << caseNumber << endl;

		for(int i = 0; i < caseNumber; ++i)
		{	
			inFile >> numA;
			inFile >> numB;
			inFile >> numK;
			allPairs.clear();
			cout << "A: " << numA << " | B: " << numB << " | K: " << numK << endl;
			for(long i = 0; i < numA; ++i)
			{
				for(long j =0; j < numB; ++j)
				{
						tempResult = i&j;
						if(tempResult < numK)
							allPairs.push_back(tempResult);
				}
			}

			//result = nValue();//!!!?
			if (outFile.is_open())
			{
				cout << "count" << count << endl;
				outFile << "Case #" << i+1 << ": " << allPairs.size()<< endl;
			}

		}

	} 
	
	outFile.close();
	inFile.close();
	return 0;
}



unsigned long And(unsigned long A, unsigned long B)
{

}
















