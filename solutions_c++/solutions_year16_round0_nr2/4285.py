#include <string>
#include <fstream>
#include <iostream>

using namespace std;

int solveTest(string s)
{
	int first = 0;
	int num = 1;
	if (s.front() == '+') first++;
	for (int i = 0; i < s.size() - 1; i++)
		if (s[i] != s[i + 1]) num++;

	if (num % 2 == 0)
	{
		if (first == 1) return num;
		if (first == 0) return num - 1;
	}
	if (num % 2 == 1)
	{
		if (first == 1) return num - 1;
		if (first == 0) return num;
	}
}

int main()
{
	ifstream f;
	f.open("B-large.in", ios::in);
	string line;
	getline(f, line);
	int t = atoi(line.c_str());

	for (int i = 0; i < t; i++)
	{
		getline(f, line);
		int n = solveTest(line);
		std::cout << "Case #" << i + 1 << ": " << n << endl;
	}
	return 0;
}