#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("b.in");
ofstream fout("b.out");

int firstUnhappy(string s)
{
	for (int i = 0; i < s.length(); i++)
		if (s[i] == '-') return i;
	return -1;
}

int lastUnhappy(string s)
{
	for (int i = s.length() - 1; i >= 0; i--)
		if (s[i] == '-') return i;
	return -1;
}

string flip(string s, int bot)
{
	string ret = s;
	for (int i = 0; i <= bot; i++)
		if (s[bot - i] == '-')
			ret[i] = '+';
		else
			ret[i] = '-';
	return ret;
}

int main()
{
	int n;
	fin >> n;
	for (int ca = 1; ca <= n; ca++) 
	{
		string st;
		fin >> st;
		
		int count = 0;
		int left = firstUnhappy(st);
		int right;
		while (left != -1) 
		{
			if (left > 0) 
			{
				count++;
				st = flip(st, left - 1);
			}
			right = lastUnhappy(st);
			if (right != -1)
			{
				count++;
				st = flip(st, right);
			}
			left = firstUnhappy(st);
		}
		fout << "Case #" << ca << ": " << count << endl;
	}
}