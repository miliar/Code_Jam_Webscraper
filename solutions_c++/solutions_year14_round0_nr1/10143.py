// MagicTrick.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>

using namespace std;

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
	stringstream ss;
	ss.str(s);
	std::string item;
	while (std::getline(ss, item, delim)) {
		elems.push_back(item);
	}
	return elems;
}

std::vector<std::string> split(const std::string &s, char delim) {
	std::vector<std::string> elems;
	split(s, delim, elems);
	return elems;
}


int _tmain(int argc, _TCHAR* argv[])
{
	fstream file;
	file.open("D:\\CJ\\A-small-attempt0.in",std::fstream::in);

	fstream output;
	output.open("D:\\CJ\\A-small-attempt0.out",fstream::out|fstream::app);

	string temp;
	getline(file, temp);

	int problems = stoi(temp);

	for(int i = 1 ; i <= problems ; i++)
	{
		int answer1;
		getline(file,temp);
		answer1 = stoi(temp) -1;

		vector< vector<string> > rows1;

		for(int j=0;j<4;j++)
		{
			getline(file,temp);
			rows1.push_back(split(temp,' '));
		}

		int answer2;
		getline(file,temp);
		answer2 = stoi(temp) -1;

		vector< vector<string> > rows2;

		for(int j=0;j<4;j++)
		{
			getline(file,temp);
			rows2.push_back(split(temp,' '));
		}

		int found =0;
		vector<string>::iterator it;
		vector<string>::iterator itResult;

		for(int j =0;j<4;j++)
		{
			it = find(rows2[answer2].begin(),rows2[answer2].end(),rows1[answer1][j]);

			if( it != rows2[answer2].end() )
				{
					found ++;
					itResult = it;
			};

		}

		if (found == 0)
		{
			output << "Case #" << i << ": Volunteer cheated!"; 
		}
		else if(found == 1)
		{
			output << "Case #" << i << ": " << *itResult;

		}
		else if(found > 1)
		{
			output << "Case #" << i << ": Bad magician!";

		}

		output << endl;

	}

	return 0;
}

