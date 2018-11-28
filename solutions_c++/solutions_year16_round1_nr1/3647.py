#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <math.h>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;

string last(string s)
{
	string t = "";
	t.push_back(s[0]);
	for (int i = 1; i < s.length(); i++)
	{
		if (s[i] < t[0])
		{
			t.push_back(s[i]);
		}
		else
		{
			t.insert(0, 1, s[i]);
		}
	}
	return t;
}

int main()
{
	ifstream infile("A-large.in");
	string line;
	int T;
	if (!(infile >> T))
	{
		cerr << "Empty file!" << endl;
		return 1;
	}
	getline(infile, line);
	ofstream outfile("A-large.out");
	for (int i = 0; i < T; i++)
	{
		if (getline(infile, line))
		{
			outfile << "Case #" << i + 1 << ": ";
			outfile << last(line) << endl;
		}
		else
		{
			cerr << "Invalid file!" << endl;
			return 1;
		}
	}
	return 0;
}