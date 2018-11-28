#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <list>
using namespace std;

int main()
{
	ifstream input;
	ofstream output;
	input.open("input.txt");
	output.open("output.txt");
	int T;
	input >> T;
	for (int cc = 0; cc < T; cc++)
	{
		string s;
		input >> s;
		list<char> answer;
		for (int i = 0; i < s.size(); i++)
		{
			char a = s[i];
			bool aisbigger = false;
			for (auto it = answer.begin(); it != answer.end(); it++)
			{
				if (a > *it)
				{
					aisbigger = true;
					break;
				}
				else if (a < *it)
				{
					break;
				}
			}
			if (aisbigger)
			{
				answer.push_front(a);
			}
			else
			{
				answer.push_back(a);
			}
		}
		output << "Case #" << cc + 1 << ": ";
		for (auto it = answer.begin(); it != answer.end(); it++)
		{
			output << *it;
		}
		output << endl;
	}
	input.close();
	output.close();
}