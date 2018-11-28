#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int reversePancake(string s)
{
	size_t pPos, mPos;
	int count = 0;
	while ((mPos = s.find_last_of('-')) != string::npos)
	{
		pPos = s.find_first_of('-');
		if (pPos > 0)
		{
			for (int i = 0; i < pPos; i++)
				s[i] = '-';
		}
		else
		{
			string newS;
			for (int i = mPos; i >=0; i--)
			{
				if (s[i] == '-')
					newS.push_back('+');
				else
					newS.push_back('-');
			}
			s = newS;
		}
		count++;
	}
	return count;
}

int main(void)
{
	fstream input, output;
	input.open("B-large.in", ios::in);
	output.open("output.txt", ios::out);
	int t;
	input >> t;
	for (int i = 1; i <= t; i++)
	{
		string s;
		input >> s;
		output <<"Case #"<<i<<": "<< reversePancake(s) << endl;
	}
	input.close();
	output.close();
	return 0;
}