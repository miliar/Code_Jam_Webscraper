//name Yufei Wang

#include <iostream>
#include <fstream>
#include <stdlib.h> 
#include <iomanip>

using namespace std;

int main (int arg, char* argv[])
{
	int numofrun = 0;
	int currentrun = 1;
	int row1 = 0;
	int row2 = 0;
	int nvm = 0;
	int arr1[4];
	int arr2[4];
	int flag =0;
	int answer = 0;
///////////////////get the code from file/////////
	string filename;
	ifstream infile;
	ofstream outfile;
	infile.open(argv[1], ios::in);
	outfile.open("result.txt", ios::out);
	if(!infile)
	 {
	  cout <<" cannot open file" ;
	  exit(0);
	  }

	if(!outfile)
	{
	  cout <<" cannot open file" ;
	  exit(0);
	 }

infile >> numofrun; ///number of tests

	 while( currentrun<= numofrun)
{
	infile >> row1;
	for (int i = 1; i < row1; ++i)
	{
		infile >> nvm;
		infile >> nvm;
		infile >> nvm;
		infile >> nvm;
	}

	for (int i = 0; i < 4; ++i)
	{
		infile >> nvm;
		arr1[i] = nvm;
	}
	for (int i = row1; i < 4; ++i)
	{
		infile >> nvm;
		infile >> nvm;
		infile >> nvm;
		infile >> nvm;
	}

	infile >> row2;
	for (int i = 1; i < row2; ++i)
	{
		infile >> nvm;
		infile >> nvm;
		infile >> nvm;
		infile >> nvm;
	}

	for (int i = 0; i < 4; ++i)
	{
		infile >> nvm;
		arr2[i] = nvm;
	}

	for (int i = row2; i < 4; ++i)
	{
		infile >> nvm;
		infile >> nvm;
		infile >> nvm;
		infile >> nvm;
	}

///////////////////////end of getting data, now searching///////////
flag = 0;

for (int i = 0; i < 4; ++i)
{
	for (int j = 0; j < 4; ++j)
	{
		if(arr1[i] == arr2[j])
		{
			if(flag == 0)
			{
				flag = 1;
				answer = arr1[i];
			}
			else if (flag ==1)
				flag = 2;
		}
	}
}

			if(flag == 1)
				outfile<<"Case #"<<currentrun<<": "<<answer<<endl;
			else if (flag ==2)
				outfile<<"Case #"<<currentrun<<": Bad magician!"<<endl;
			else if (flag ==0)
				outfile<<"Case #"<<currentrun<<": Volunteer cheated!"<<endl;
			else
				outfile<<"bug"<<endl;





/*
		outfile <<hex << table[0];
		for (int i = 1; i < 4; ++i)
		{
			if (table[i] != 0)
			{
				outfile <<hex <<" "<< table[i];
			}
		}
		outfile <<endl;
	*/


	
	currentrun++;
}////eof

   infile.close();
   outfile.close();
return 0;
}


