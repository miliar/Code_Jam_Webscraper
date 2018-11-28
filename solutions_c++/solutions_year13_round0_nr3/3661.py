#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

bool isPal(int num);

int main()
{
	ifstream fin("C-small.in");
	ofstream fout("C_small.out");

	int cases;
	fin >> cases;

	for (int i=0; i<cases; ++i)
	{
		fout << "Case #" << i+1 << ": ";

		int min, max;
		fin >> min >> max;

		if (sqrt(min) == static_cast<int>(sqrt(min)))
			min = sqrt(min);
		else
			min = sqrt(min) + 1;
		max = sqrt(max) + 1;

		int count = 0;
		for (int num=min; num<max; ++num)
		{
			if (isPal(num) && isPal(pow(num,2)))
				++count;
		}

		fout << count << endl;
	}

	return 0;
}

bool isPal(int num)
{
	stringstream ss;
	ss << num;
	string number = ss.str();

	for (int i=0; i<number.size()/2; ++i)
	{
		if (number[i] != number[number.size()-i-1])
			return false;
	}
	return true;
}