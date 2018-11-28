#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <math.h>
#include <map>
#include <vector>
#include <fstream>
#include <stdint.h>
#include <float.h>
using namespace std;

int main()
{
	ifstream input;
	ofstream output;
	ifstream binary;
	fstream rules;
	input.open("A-large.in");
	binary.open("binary.txt");
	rules.open("rules.txt",ios::out|ios::in);
	output.open("test.on");
	int t;
	input >> t;
	for (int i = 0; i < t; i++)
	{
		string x;
		input >> x;
		string out = "";
		char max = 'A';
		for (int k = 0; k < x.size(); k++)
		{
			if (x[k] < max)
			{
				out = out + x[k];
				if (k == 0)
				{
					max = x[k];
				}
			}
			else
			{
				out = x[k] + out;
				max = x[k];
			}
		}
		output << "Case #" << i+1 << ": " << out<<endl;
	}
	return 0;
}
