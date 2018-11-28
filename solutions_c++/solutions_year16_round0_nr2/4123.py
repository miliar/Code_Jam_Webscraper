// Problem B - Revenge of the Pancakes

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream fin("B-large.in");
	ofstream fout ("B-large.txt");
	int t;
	fin >> t;
	string s;
	for (int i = 0; i < t; i++)
	{
		fin >> s;
		fout << "Case #" << i + 1 << ": ";
		s += '+';
		int cnt = 0;
		for (int j = 0; j < s.length() - 1; j++)
		{
			if (s[j] != s[j + 1]) 
				cnt++;
		}
		fout << cnt << endl;
	}

	return 0;
}
