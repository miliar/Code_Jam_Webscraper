#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
#include <cmath>

using namespace std;

int main()
{
	int num_test=0;
	ifstream fin("A-small-attempt3.in");
	ofstream fout("outputtest.txt");
	
	fin>>num_test;
	
	for(int i=0;i<num_test;i++)
	{
		int matrix[4][4], matrix_second[4][4];
		int first_row=0, second_row=0, value=0, counter=0;
		fin>>first_row;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				fin>>matrix[j][k];
			}
		}
		
		
		fin>>second_row;

		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				fin>>matrix_second[j][k];
			}
		}
		
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(matrix[first_row-1][j]==matrix_second[second_row-1][k])
				{
					value= matrix[first_row-1][j];
					counter++;
					
				}
			}
			
		}
		
		if(counter==0)
		fout<<"Case #"<<i+1<< ": Volunteer cheated!"<<endl;
		
		else if (counter==1)
		fout<<"Case #"<<i+1<<": "<<value<<endl;
		
		else
		fout<<"Case #"<<i+1<<": Bad magician!"<< endl;
	}
	
	return 0;
	
}

