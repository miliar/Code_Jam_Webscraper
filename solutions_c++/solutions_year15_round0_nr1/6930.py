#include<stdlib.h>
#include<fstream>
#include<iostream>
#include<string>

using namespace std;

void main()
{
	ifstream fin;
	ofstream fout;
	fin.open("D:/inputsmall.txt");
	fout.open("D:/output.txt");
	int totalnum;
	int smax;
	fin >> totalnum;
	int standnum = 0;
	int friendnum = 0;
	for (int i = 0; i < totalnum; i++)
	{
		standnum = 0;
		friendnum = 0;
		fin >> smax;
		string audinence;
		fin >> audinence;
		for (int j = 0; j < audinence.size(); j++)
		{
			if (j > 0)
			{
				while (standnum < j)
				{
					standnum++;
					friendnum++;
				}		
			}
			standnum += (int)audinence[j] - 48;
			//cout << standnum << " ";			
		}
		fout << "Case #" << i + 1 << ": " << friendnum << endl;
	}
	//string test = "09";
	//cout << (int)test[0] - 48;
	fin.close();
	fout.close();
}