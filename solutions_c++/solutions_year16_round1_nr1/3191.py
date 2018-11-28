#include <string>
#include <fstream>
#include <iostream>
using namespace std;

int main()
{
	int t;
	ifstream in("A-large.in");
	ofstream out("out.txt");
	in >> t;
	string input;
	for (int i = 1; i <= t; i++)
	{
		in >> input;
		string output = input.substr(0, 1);
		for (int j = 1; j < input.length(); j++)
		{
			if (input.at(j) >= output.at(0))
			{
				output = input.substr(j, 1) + output;
			}
			else
			{
				output += input.substr(j, 1);
			}
		}

		out << "Case #" << i << ": " << output << endl;
	}
}