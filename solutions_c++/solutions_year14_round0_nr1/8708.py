
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

int cards_first[4][4];
int cards_second[4][4];

int main()
{
	ifstream fin;
	fin.open("A-small-attempt1.in");
	ofstream fout;
	fout.open("A-small-attempt1.out");
	int t;
	fin>>t;
	for(int c = 0; c<t; c++)
	{
		int first, second;
		vector<int> interset;
		fin>>first;
		for(int i = 0; i<4; i++)
			for(int j = 0; j<4; j++)
				fin>>cards_first[i][j];
		fin>>second;
		for(int i = 0; i<4; i++)
			for(int j = 0; j<4; j++)
				fin>>cards_second[i][j];
		for(int i = 0; i<4; i++)
		{
			for(int j = 0; j<4; j++)
			{
				if(cards_second[second-1][j] == cards_first[first-1][i])
					interset.push_back(cards_second[second-1][j]);
			}
		}
		if(interset.size() == 1)
			fout<<"Case #"<<c+1<<": "<<interset[0]<<endl;
		else if(interset.size() == 0)
			fout<<"Case #"<<c+1<<": Volunteer cheated!\n";
		else
			fout<<"Case #"<<c+1<<": Bad magician!\n";
	}
	fin.close();
	fout.close();
	return 0;
}

