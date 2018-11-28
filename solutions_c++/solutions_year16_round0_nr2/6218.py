#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int flipNumber(string s)
{
	if (s.size() == 1)
	{
		if (s == "+")
			return 0;
		else
		{
			return 1;
		}
	}
	int count = 0;
	for (size_t i = 1; i < s.size(); i++)
	{
		if (s[i] != s[i - 1])
		{
			count++;
		}
	}
	if (s.back() == '-')
	{
		count++;
	}
	return count;
}

int main()
{

	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	string panck;
	fin >> panck;
	int count = 1;
	while (fin >> panck)
	{
		fout << "Case #" << count << ": " << flipNumber(panck) << endl;
	
		count++;
	}
	return 0;
}