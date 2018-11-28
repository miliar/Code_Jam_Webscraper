#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int noOfTestcases;
	int rowNum,rowNum1;
	int** arr = new int*[4];
	for(int i=0 ; i< 4 ; i++)
	{
		arr[i]=new int[4];
	}
	int** arr1 = new int*[4];
	for(int i=0 ; i< 4 ; i++)
	{
		arr1[i]=new int[4];
	}
	fstream dataFile;
	ofstream out;
	system("cls");
	dataFile.open("A-small-attempt1.in");
	out.open("output.txt");
	if(!dataFile)
	{
		cout << "File Not Found" << endl;
		exit(0);
	}
	int count=0;
	int TC=1;
	int result;
	dataFile >> noOfTestcases;
	for(int i =0 ; i < noOfTestcases ;i++)
	{
		dataFile >> rowNum;
		for(int j = 0 ; j < 4 ; j++)
		{
			for(int k = 0 ; k < 4 ; k++)
				dataFile >> arr[j][k];
		}
		dataFile >> rowNum1;
		for(int j = 0 ; j < 4 ; j++)
		{
			for(int k = 0 ; k < 4 ; k++)
				dataFile >> arr1[j][k];
		}
		for(int j=0 ; j < 4 ; j++)
		{
			for(int k=0 ; k < 4 ; k++)
			{
				if (arr[rowNum-1][j]==arr1[rowNum1-1][k])
				{
					result=arr[rowNum-1][j];
					count++;
				}
			}
		}
		if(count == 1)
		{
			out<< "Case #" << TC << ": " << result<<endl;
		}
		else if(count > 1)
		{
			out<< "Case #" << TC << ": Bad magician!"<<endl;
		}if(count < 1)
		{
			out<< "Case #" << TC << ": Volunteer cheated!"<<endl;
		}
		TC++;
		count=0;
	}
	return 0;
}