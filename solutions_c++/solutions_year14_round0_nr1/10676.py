#include <iostream>
#include <fstream> 

using namespace std;

void Readin ( ifstream & fin, int vin, int card[])
{
	int temp;
	for (int i=0; i<4; i++)
	{
		for (int j = 0 ; j<4; j++)
		{
			if (i+1 == vin)
			{
				fin >> card[j];
			}
			else
			{
				fin >> temp;
			}
		}
	}
}

void Compare (int first[],int second[], int & num, int & count)
{
	count = 0;
	for (int i=0; i<4; i++)
	{
		for (int j=0; j<4; j++)
		if (first[i] == second[j])
		{
			count++;
			num = first[i];
		}
		
	}
}

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout ("output.txt");
	
	int casecount = 0,count;
	int x;
	int num;
	int vin1, vin2;
	int first[4], second[4];
	
	fin >> x;
	
	for (int i=0; i<x; i++)
	{
		fin >> vin1;
		Readin (fin, vin1, first);
		fin >> vin2;
		Readin (fin, vin2, second) ;
		
		Compare (first, second, num, count);
		
		fout << "Case #" << i+1 << ": ";
		if (count == 1)
		{
			 fout << num;
		}
		
		else if (count >1)
		{
			fout << "Bad magician!";
		}
		
		else if (count ==0)
		{
			fout << "Volunteer cheated!";
		}
		
		
		fout << endl;
		
	}
	
	
	
	
}
