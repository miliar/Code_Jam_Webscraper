#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;

bool check(string pancakes)
{
	for (int i = 0; i < pancakes.size(); i++)
	{
		if (pancakes[i]=='-')
		{
			return false;
		}
	}
	return true;
}

string flipStack(string pancakes, int end)
{
	string fliped = "";
	for (int i = end; i >= 0; i--)
	{
		fliped += pancakes[i] == '-' ? '+' : '-';
	}
	for (int i = 0; i <= end; i++)
	{
		pancakes[i] = fliped[i];
	}
	return pancakes;
}
int main()
{
	fstream fin;
	fstream fout;
	fin.open("B-large.in", ios::in);
	fout.open("B-large.out", ios::out);

	int t;
	fin >> t;
	for (int i = 0; i < t; i++)
	{
		string pancakes;
		fin >> pancakes;
		int count = 0;
		while (!check(pancakes))
		{
			for (int i = pancakes.size()-1; i >=0; i--)
			{
				if (pancakes[i]=='-' && pancakes[0]=='-')
				{
					pancakes = flipStack(pancakes, i);

					count++;
					break;
				}
				else if (pancakes[i]=='-')
				{
					int x = 0;
					while (x < pancakes.size() && pancakes[x] =='+')
					{
						pancakes[x] = '-';
						x++;
					}
					count++;
					pancakes = flipStack(pancakes, i);
					count++;
					break;
				}
			}
		}
		fout << "Case #" << (i + 1) << ": " << count << endl;
	}
	return 0;
}