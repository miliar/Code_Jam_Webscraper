#include <iostream>
#include <string>
#include <fstream>
using namespace std;

string getResults(string input)
{
	string tempString = "";
	if(input.length() == 0) return tempString;
	else
	{
		char *temp = &input.at(0);
		for (int i = 0; i < input.length(); i++)
		{
			if(input.at(i) >= *temp)
			{
				string ts = input.substr(i, 1);
				int pos = 0;
				if(tempString.length() > 0 && (ts.at(0) >= tempString.at(0))) pos = 0;
				else pos = -1;

				if(pos == 0) tempString.insert(0, ts);
				else tempString.append(ts);
			}
			else
			{
				tempString.append(input.substr(i, 1));
			}
		}
		return tempString;
	}
}

int main()
{
	ifstream fin("round1-a-1.txt");
	ofstream fout("output-round1-a-1.txt");

	int testcases;
	fin >> testcases;

	for(int i = 0; i < testcases; i++)
	{
		string input;
		fin >> input;

		fout << "Case #" << i+1 << ": " << getResults(input) << endl;
	}
	return 0;
}