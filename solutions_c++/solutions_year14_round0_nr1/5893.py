#include <iostream>
#include <fstream>

#include <list>


using namespace std;

//Card Matrixs
int beforeCards[4][4];
int afterCards[4][4];
list<int> diference;


//Number of cases
int nCases;
int selectedFirst;
int selectedSecond;

int main(int argc, char *argv[])
{
	ifstream fileIn;
	ofstream fileOut;
	fileIn.open("in.txt");
	fileOut.open("out.txt");

	//Read number of cases
	
	fileIn >> nCases;
	
	
	for(int i=0;i<nCases;i++)
	{
		diference.clear();

		fileIn >> selectedFirst;
		//Read before
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				fileIn >> beforeCards[j][k];
			}
		}

		fileIn >> selectedSecond;
		//Read after
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				fileIn >> afterCards[j][k];
			}
		}
		//compare the lines
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(beforeCards[selectedFirst-1][j] == afterCards[selectedSecond-1][k])
				{
					diference.push_back(beforeCards[selectedFirst-1][j]);
				}
			}
		}

		cout << "Case #" << i+1 << ": ";
		fileOut << "Case #" << i+1 << ": ";
		if(diference.size() > 1)
		{
			cout << "Bad magician!";
			fileOut << "Bad magician!";
		}
		else if (diference.size() == 0)
		{
			cout << "Volunteer cheated!";
			fileOut << "Volunteer cheated!";
		}
		else
		{
			cout << diference.front();
			fileOut << diference.front();
		}
		
		cout << "\n";
		fileOut << "\n";
	}

	fileOut.close();
	system("pause");
}