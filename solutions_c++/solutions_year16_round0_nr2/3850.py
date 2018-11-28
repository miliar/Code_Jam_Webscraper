#ifndef S
#define S 100
#endif

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int moves(string s)
{
	int pos, len;
	for (int i = s.length(); i > 0; i--)
	{
		if (i == 1)
		{
			if (s[0] == '+')
			{
				return 0;
			}
			else
			{
				return 1;
			}
		}
		if (s[i - 1] != s[i - 2])
		{
			pos = i - 1;
			len = s.length() - pos;
			break;
		}
	}
	if (s[pos] == '+')
	{
		s.erase(pos, len);
		return moves(s);
	}
	else
	{
		s.erase(pos, len);
		return moves(s) + 2;
	}
}

int main(int argc, char const *argv[])
{
	ifstream infile("B-large.in");
	string line;
	int T;
	if (!(infile >> T))
	{
		cerr << "Empty file!" << endl;
		return 1;
	}
	getline(infile, line);
	ofstream outfile("B-large.out");
	for (int i = 0; i < T; i++)
	{
		if (getline(infile, line))
		{
			outfile << "Case #" << i + 1 << ": ";
			outfile << moves(line) << endl;
		}
		else
		{
			cerr << "Invalid file!" << endl;
			return 1;
		}
	}
	return 0;
}