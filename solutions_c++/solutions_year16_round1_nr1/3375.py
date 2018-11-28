#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	ifstream fin("file.in");
	ofstream fout("file.out");
	int CASES;
	fin >> CASES;

	for (int CASE = 1; CASE <= CASES; CASE++)
	{
		string foo;
		fin >> foo;
		vector<char> answer;
		answer.push_back(foo[0]);
		for (int i = 1; i < foo.length(); i++)
		{
			if (foo[i] >= answer[0])
			{
				answer.insert(answer.begin(), foo[i]);
			}
			else
			{
				answer.push_back(foo[i]);
			}
		}
		fout << "Case #" << CASE << ": ";
		for (int i = 0; i < answer.size(); i++)
		{
			fout << answer[i];
		}
		fout << endl;
	}
}