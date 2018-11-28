#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <sstream>

using namespace std;


int lineCount = 0;
int loopCount = 0;
int *inputs;
string line = " ";
int arr[] = {0,0,0,0,0,0,0,0,0,0};
ofstream outfile;

int calc(int num);
bool isFilled(int a[10]);
void breaking(int val);
void resetArray();

int main(int argc,char *argv[])
{

	string inputFile = argv[1];

	ifstream myfile(inputFile.c_str());

	if (myfile.is_open())	// when file open
	{
		while(getline(myfile,line))	// for each line of the file
		{
			if(lineCount == 0)
			{
				loopCount = atoi(line.c_str());
				inputs = new int[loopCount];
			}

			else
			{
				for (int i =0;i < loopCount;i++)
				{
					inputs[i] = atoi(line.c_str());
					getline(myfile,line);
				}
			}
			lineCount++;
		}
	}



	outfile.open("output.txt",std::fstream::app); // define the outfile with given name

	for (int j =0 ; j< loopCount;j++)
	{
		outfile << "Case #" << (j+1) << ": ";
		int result = calc(inputs[j]);
		if (result == -1)
			outfile << "INSOMNIA";
		else
			outfile << result;
		outfile << endl;
	}

	outfile.close();

	return 0;
}


bool isFilled()
{
	for(int i = 0;i<10;i++)
	{
		if (arr[i] == 0)
			return false;
	}

	return true;
}

int calc(int num)
{
	int N = num;
	int multiplier = 1;
	while(isFilled() == false)
	{	
		N = multiplier * num;
		breaking(N);
		multiplier++;

		if(multiplier > 10000000)
		{
			resetArray();
			return -1;
		}
		
	}

	resetArray();
	return N;

}

void resetArray()
{
	for(int i = 0;i<10;i++)
	{
		arr[i] = 0;
	}
}


void breaking(int val)
{	
	stringstream ss;
	ss << val;
	string strVal  = ss.str();



	for(int i = 0;i< strVal.size();i++)
	{
		switch(strVal[i])
		{
			case '0':
				arr[0] = 1;
				break;
			case '1':
				arr[1] = 1;
				break;
			case '2':
				arr[2] = 1;
				break;
			case '3':
				arr[3] = 1;
				break;
			case '4':
				arr[4] = 1;
				break;
			case '5':
				arr[5] = 1;
				break;
			case '6':
				arr[6] = 1;
				break;
			case '7':
				arr[7] = 1;
				break;
			case '8':
				arr[8] = 1;
				break;
			case '9':
				arr[9] = 1;
				break;
		}
	}
}