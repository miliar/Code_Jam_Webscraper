#include<iostream>
#include <fstream>
#include<cstring>
#include<conio.h>
#include <sstream>

using namespace std;
typedef unsigned int uint;

int main()
{
	uint testcases;
	string line;
	ifstream in("E:\\B-small-attempt0.in", ios::in);
	ofstream out("E:\\testout.in", ios::out);

	uint a, b, k, temp[3],t;

	getline(in, line);
	stringstream ss(line);
	ss >> testcases;

	for (uint i = 1; i <= testcases; i++)
	{
		getline(in, line);
		stringstream ss1(line);
		uint j = 0;
		while (ss1 >> t)
		{
			temp[j] = t;
			j++;
		}

		a = temp[0];
		b = temp[1];
		k = temp[2];
		uint win = 0;
		for (uint j = 0; j < a; j++)
		{
			for (uint r = 0; r < b; r++)
			{
				uint t = (j&r);
				if (t < k)
					win++;
			}
		}
		out << "Case #" << i << ": " << win << endl;
	}
}