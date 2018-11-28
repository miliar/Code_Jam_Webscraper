// Problem A - Counting Sheep

#include <iostream>
#include <fstream>
using namespace std;

bool digits[10];

void process(long long n)
{
	long long m = n;
	while (m > 0)
	{
		digits[m % 10] = true;
		m /= 10;
	}
}

bool check()
{
	for (int i = 0; i < 10; i++)
	{
		if (!digits[i]) return false;
	}
	return true;
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout ("A-large.txt");
	int t;
	fin >> t;
	long long n;
	for (int i = 0; i < t; i++)
	{
		fin >> n;
		fout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < 10; j++) 
			digits[j] = false;
		if (n == 0)
		{
			fout << "INSOMNIA" << endl;
			continue;
		}
		// will always terminate
		long long last = 0;
		while (!check())
		{
			last += n;
			process(last);
		}
		fout << last << endl;
	}
	return 0;
}
