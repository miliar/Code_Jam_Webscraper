// 2016QualificationRound.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>

using namespace std;

int main()
{
	std::ifstream fs("data/D-small-attempt0.in");

	int t;

	fs >> t;

	for (auto i = 1; i <= t; i++)
	{
		int k, c, s;
		fs >> k >> c >> s;

		cout << "Case #" << i << ": ";

		for (int j = 1; j <= s; j++)
			cout << j << " ";
		cout << endl;
	}

	return 0;
}

