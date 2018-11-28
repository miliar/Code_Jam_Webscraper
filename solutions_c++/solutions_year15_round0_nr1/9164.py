#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	ifstream file_in("A-large.in");
	ofstream file_out("output.txt");
	int cases;
	file_in >> cases;
	for (int i = 1; i <= cases; i++)
	{
		int shy;
		file_in >> shy;
		string audience;
		file_in >> audience;
		int value[1001];
		for (int j = 0; j <= shy ; j++)
		{
			value[j] = audience.at(j) - '0';
		}

		int cur = 0;
		int sum = 0;
		for (int j = 0; j <= shy; j++)
		{
			if (cur < j)
			{
				int need = j - cur;
				cur = j;
				sum += need;
			}
			cur += value[j];
		}

		file_out << "Case #" << i << ": " << sum << endl;

	}
	return 0;
}