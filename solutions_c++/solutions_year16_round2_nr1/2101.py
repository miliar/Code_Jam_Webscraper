#include <iostream>
#include <vector>
#include <ctime>
#include <fstream>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	fstream in("in.in"), out("out.txt");


	int T;
	string line;

	in >> T;

	getline(in, line, '\n');

	for (int t = 1; t <= T; ++t)
	{
		int letters[26];
		memset(letters, 0, sizeof(letters));
		vector<int> res;

		getline(in, line, '\n');

		for (int i = 0; i < line.length(); ++i)
			letters[line[i] - 'A']++;

		while (letters['Z' - 'A'] > 0) 
		{
			res.push_back(0);
			letters['Z' - 'A']--;
			letters['E' - 'A']--;
			letters['R' - 'A']--;
			letters['O' - 'A']--;
		}

		while (letters['W' - 'A'] > 0) 
		{
			res.push_back(2);
			letters['T' - 'A']--;
			letters['O' - 'A']--;
			letters['W' - 'A']--;
		}

		while (letters['X' - 'A'] > 0) 
		{
			res.push_back(6);
			letters['S' - 'A']--;
			letters['I' - 'A']--;
			letters['X' - 'A']--;
		}

		while (letters['G' - 'A'] > 0) 
		{
			res.push_back(8);
			letters['E' - 'A']--;
			letters['I' - 'A']--;
			letters['G' - 'A']--;
			letters['H' - 'A']--;
			letters['T' - 'A']--;
		}

		while (letters['U' - 'A'] > 0) 
		{
			res.push_back(4);
			letters['F' - 'A']--;
			letters['O' - 'A']--;
			letters['U' - 'A']--;
			letters['R' - 'A']--;
		}

		while (letters['F' - 'A'] > 0) 
		{
			res.push_back(5);
			letters['F' - 'A']--;
			letters['I' - 'A']--;
			letters['V' - 'A']--;
			letters['E' - 'A']--;
		}

		while (letters['V' - 'A'] > 0) 
		{
			res.push_back(7);
			letters['S' - 'A']--;
			letters['E' - 'A']--;
			letters['V' - 'A']--;
			letters['E' - 'A']--;
			letters['N' - 'A']--;
		}

		while (letters['O' - 'A'] > 0) 
		{
			res.push_back(1);
			letters['O' - 'A']--;
			letters['N' - 'A']--;
			letters['E' - 'A']--;
		}

		while (letters['N' - 'A'] > 0) 
		{
			res.push_back(9);
			letters['N' - 'A']--;
			letters['I' - 'A']--;
			letters['N' - 'A']--;
			letters['E' - 'A']--;
		}

		while (letters['T' - 'A'] > 0) 
		{
			res.push_back(3);
			letters['T' - 'A']--;
			letters['H' - 'A']--;
			letters['R' - 'A']--;
			letters['E' - 'A']--;
			letters['E' - 'A']--;
		}

		sort(res.begin(), res.end());

		out << "Case #" << t << ": ";

		for (int i = 0; i < res.size(); ++i)
			out << res[i];

		out << endl;
	}

	in.close();
	out.close();

	return 0;
}