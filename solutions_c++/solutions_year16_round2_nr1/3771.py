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

vector<int> digits;
const string numbers[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

void vec_print(vector<int> vec)
{
	for (int i = 0; i < vec.size(); i++)
	{
		cout << vec[i] << ' ';
	}
	cout << endl;
}

string search(string p, string c)
{
	vector<int> pos;
	string bak = p;
	bool find, match;
	match = true;
	for (int i = 0; i < c.length(); i++)
	{
		find = false;
		for (int j = 0; j < p.length(); j++)
		{
			if (p[j] == c[i])
			{
				p[j] = '*';
				pos.push_back(j);
				find = true;
				break;
			}
		}
		if (!find)
		{
			match = false;
			break;
		}
	}
	if (match)
	{
		p = bak;
		sort(pos.begin(), pos.end());
		//vec_print(pos);
		for (int i = 0; i < c.length(); i++)
		{
			p.erase(p.begin() + pos[i]);
			for (int j = i + 1; j < c.length(); j++)
			{
				pos[j] -= 1;
			}
		}
		return p;
	}
	else
	{
		return "!";
	}
}

bool reduce(string line, int curr)
{
	if (line.empty())
	{
		return true;
	}
	string line_bak = line;
	int curr_bak = curr;
	string num, res;
	for (int i = curr; i < 10; i++)
	{
		num = numbers[i];
		res = search(line, num);
		if (res != "!")
		{
			digits.push_back(i);
			line = res;
			curr = i;
			if (reduce(line, curr))
			{
				return true;
			}
			else
			{
				digits.pop_back();
				line = line_bak;
				curr = curr_bak;
			}
		}
	}
	if (res == "!")
	{
		return false;
	}
}

int main()
{
	ifstream infile("A-small-attempt1.in");
	string line;
	int T;
	if (!(infile >> T))
	{
		cerr << "Empty file!" << endl;
		return 1;
	}
	getline(infile, line);
	ofstream outfile("A-small-attempt1.out");
	for (int i = 0; i < T; i++)
	{
		if (getline(infile, line))
		{
			//string halt(line.length(), '*');
			digits.clear();
			reduce(line, 0);
			outfile << "Case #" << i + 1 << ": ";
			for (int i = 0; i < digits.size(); i++)
			{
				outfile << digits[i];
			}
			outfile << endl;
		}
		else
		{
			cerr << "Invalid file!" << endl;
			return 1;
		}
	}

	return 0;
}