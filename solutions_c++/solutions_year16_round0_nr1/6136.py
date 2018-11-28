#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int lastnumber(int number)
{
	int number0 = number;
	vector<bool> checked;
	checked.resize(10, false);
	int total_check = 0;
	while (total_check != 10)
	{
		int num = number;
		while (num >= 10)
		{
			int dig = num % 10;
			if (!checked[dig])
			{
				checked[dig] = true;
				total_check++;
			}
			num = num / 10;
		}
		if (!checked[num])
		{
			checked[num] = true;
			total_check++;
		}
		if (total_check != 10)
		{
			number += number0;
		}
	}
	//cout << number << endl;
	return number;
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int digit;
	int count = 1;
	fin >> digit;
	while (fin >> digit)
	{
		if (digit == 0)
		{
			fout << "Case #" << count << ": INSOMNIA" << endl;
		}
		else
		{
			fout << "Case #" << count << ": " << lastnumber(digit) << endl;
		}
		count++;
	}

	return 0;
}