#include <string>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


int compvar(const void *one, const void *two)
{
    float a = *((float*)one);
    float b = *((float*)two);
    if (a>b)
       return -1;
    if (a == b)
       return 0;
    return 1;   

}

int main()
{
	string line;
	ifstream myReadFile;
	ofstream myfile;
	myfile.open ("output.txt");
	myfile.clear();
 
	myReadFile.open("D-large.in");
	int numberOfTest;
	myReadFile >> numberOfTest;
	getline(myReadFile,line);
	vector<float> blockListA;
	vector<float> blockListB;
	//vector<float> deceifulWarListA;
	//vector<float> deceifulWarListB;
	int numberOfVictoryWar, numberOfVictoryDecWar;
	for (int i = 0; i< numberOfTest; i++)
	{
		numberOfVictoryDecWar=numberOfVictoryWar=0;
		blockListA.clear();
		blockListB.clear();
		int numberOfBlock;
		myReadFile>>numberOfBlock;
		float tmp;
		for(int i =0; i< numberOfBlock; i++)
		{
			myReadFile>>tmp;
			blockListA.push_back(tmp);
		}
		for(int i =0; i< numberOfBlock; i++)
		{
			myReadFile>>tmp;
			blockListB.push_back(tmp);
		}

		qsort(&blockListA[0],blockListA.size(),sizeof(float),compvar);
		qsort(&blockListB[0],blockListB.size(),sizeof(float),compvar);

		///////Find number of victory in War strategy
		int i1,j1,i2,j2;
		i2=0;
		j2=blockListB.size() - 1;
		for (i1=0; i1<blockListA.size();i1++)
		{
			if(blockListA[i1] > blockListB[i2])
			{
				numberOfVictoryWar++;
				j2--;
			}
			else
				i2++;
		}

		////////Find number of victory in Deceiful War strategy
		i1 = 0;
		j1 = blockListA.size() - 1;
		for (i2 = 0; i2<blockListB.size(); i2++)
		{			
			if(blockListB[i2] > blockListA[i1])
			{
				j1--;
			}
			else
			{
				numberOfVictoryDecWar++;
				i1++;
			}
		}

		myfile<< "Case #" << i + 1 <<": ";
		myfile<<numberOfVictoryDecWar<<" "<<numberOfVictoryWar;
		myfile<<endl;

	}

	myReadFile.close();  
	myfile.close();
	return 0;
}