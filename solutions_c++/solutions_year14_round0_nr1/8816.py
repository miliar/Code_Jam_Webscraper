//Melissa Serrano
//Melster

#include <list>
#include <string>
#include <cctype>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iomanip> 
using namespace std;

void main()
{
	int t;
	int row;
	int notused;
	int val;

	ifstream filein;
	filein.open("A-small-attempt0.in");
	if (!filein.is_open()) return;

	ofstream fileout;
	fileout.open("Aout.txt");
	if (!fileout.is_open()) return;

	filein >> t;

	for (int i = 1; i <= t; i++)
	{
		ostringstream strst;
		strst << i;
		string st = strst.str();
		string returns = "Case #" + st + ": ";
		fileout<<returns;
		filein >> row;

		vector<int> vect1;
		int pos = row-1;
		for(int j=0; j<(pos*4);j++)
		{
			filein >> notused;
		}
		for(int j=0; j<4;j++)
		{
			filein >> val;
			vect1.push_back(val);
		}
		pos = 4 - row;
		for(int j = 0; j<(pos*4); j++)
		{
			filein >> notused;
		}

		vector<int> vect2;
		filein >> row;
		pos = row-1;
		for(int j=0; j<(pos*4);j++)
		{
			filein >> notused;
		}
		for(int j=0; j<4;j++)
		{
			filein >> val;
			vect2.push_back(val);
		}
		pos = 4 - row;
		for(int j = 0; j<(pos*4); j++)
		{
			filein >> notused;
		}

		sort(vect1.begin(), vect1.end());
		sort(vect2.begin(), vect2.end());
		int matchval;
		int count = 0;
		int i1 = 0;
		int j2 = 0;//vect2.size()-1;
	
		while((i1<=vect1.size()-1) && (j2<=vect1.size()-1))//>=0))
		{
			if(vect1[i1] == vect2[j2])
			{
				matchval = vect1[i1];
				count++;
			}
			if(vect1[i1] < vect2[j2])
			{
				i1++;
			}
			else//if(vect1[i1] > vect2[j2])
			{
				j2++;//--;
			}
		}
		if(count == 0)
		{
			fileout<<"Volunteer cheated!\n";
		}
		if(count == 1)
		{
			fileout<<matchval<<endl;
		}
		if(count > 1)
		{
			fileout<<"Bad magician!\n";
		}
	}
	fileout.close();
	filein.close();
	return;
}