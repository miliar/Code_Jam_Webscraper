#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

//Function Declarations
bool loadFile (string, int &, long long int *, long long int *);
bool saveFile (string, int, long long int *);
void check (int, long long int *, long long int *, long long int *);

int main(int argc, char *argv[]) 
{
	long long int radius[6000], paint[6000], numberOfRings[6000];
	int numberOfCases;
	bool error;
	
	error = loadFile ("input.in", numberOfCases, radius, paint);
	
	if (error)
	{
		check (numberOfCases, radius, paint, numberOfRings);
		saveFile ("output.txt", numberOfCases, numberOfRings);
	}
	
	return 0;
}

bool loadFile (string fileName, int &numberOfCases, long long int *radius, long long int *paint)
{
	int i;
	ifstream fin;
	
	fin.open(fileName.c_str());
	if (fin.is_open())
	{
		fin >> numberOfCases;
		for (i=0; i<numberOfCases; i++)
			fin >> radius[i] >> paint[i];
	}
	else
	{
		fin.close();
		return false;
	}
	fin.close();
	return true;
}

bool saveFile (string fileName, int numberOfCases, long long int *numberOfRings)
{
	int i;
	ofstream fout;
	
	fout.open(fileName.c_str());
	if (fout.is_open())
	{
		for (i=0; i<numberOfCases; i++)
		{
			fout << "Case #" << i+1 << ": " << numberOfRings[i] << endl;
		}
	}
	else
	{
		fout.close();
		return false;
	}
	fout.close();
	return true;
}

void check (int numberOfCases, long long int *radius, long long int *paint, long long int *numberOfRings)
{
	int i;
	long long int count, number;
	bool enough;
	
	for (i=0; i<numberOfCases; i++)
	{
		count=0;
		enough=true;
		cout << i+1 << " ";
		while (enough)
		{
			number = 2 * radius[i] + 1;
			if (paint[i]>=number)
			{
				paint[i] -= number;
				radius[i]+=2;
				count++;
			}
			else
			{
				numberOfRings[i] = count;
				enough = false;
			}
		}
		cout << count << endl;
		numberOfRings[i]=count;
	}
}
