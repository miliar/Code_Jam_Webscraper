#include <iostream>
#include <iomanip>
#include <cstring>
#include <string>
#include <cstdio>
#include <fstream>
using namespace std;
const int MAX = 1001;
int main()
{
	int T = 0;
	int count = 0;
	char shy[MAX];
	string shyness;
	int maxshy;
	char temp;
	char tempstr[1];
	int tempin = 0;
	int temp2;
	int temp3 = 0; // stores total
	int count2; //index of shyness
	int invite = 0;
	int ttlinvite = 0;
	ifstream fin;
	ofstream fout;

	fin.open("A-large.in");
	fout.open("largeinput.out");

	do
	{
		
		fin >> T;

	} while (T < 1 || T > 100);
	
	while (count < T)
	{
		do
		{
		
			fin >> maxshy;
		} while (maxshy < 0 || maxshy > 1000);
		do
		{
		
			fin >> shyness;
		} while ((shyness.size()) > maxshy + 1);
		tempin = 0;
		do
		{
			ttlinvite += invite;
			
			
			tempstr[0] = shyness[tempin];
			temp2 = atoi(tempstr);
			temp3 += temp2 + invite;
			invite = 0;
			if (tempin == 0 && temp2 == 0)
			{
				invite = 1;
			}

			if (tempin != 0 && temp3 < (tempin + 1) && tempin != maxshy)
			{
				invite = (tempin + 1) - temp3;
			}
			


		
			
			tempin++;
			
		} while (tempin <= maxshy);
		fout << "Case #" << count + 1 << ": " << ttlinvite << endl;
		invite = 0;
		ttlinvite = 0;
		temp3 = 0;
		count++;
	}
	fin.close();
	fout.close();
	return 0;

}