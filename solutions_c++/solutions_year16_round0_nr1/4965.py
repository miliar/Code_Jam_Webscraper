#include <iostream>
#include <fstream>
#include <vector>
#include <fstream>
using namespace std;

void createExtreamTestCase(fstream& fout,int start, int end)
{
	fout << end - start << endl;
	for (int i = start; i <= end; i++)
	{
		fout << i << endl;
	}

}
bool check(vector<bool> digits)
{
	for (int i = 0; i < digits.size(); i++)
		if (digits[i] == false)
			return false;

	return true;
}
vector<int> getDigits(long long num)
{
	vector<int> digits;
	while (num > 0)
	{
		int digit = num % 10;
		num /= 10;
		digits.push_back(digit);
	}
	return digits;
}
long long getLastNum(long long num)
{
	vector<bool> digits(10, 0);
	vector<int> outDigits = getDigits(num);
	for (int i = 0; i < outDigits.size(); i++)
	{
		digits[outDigits[i]] = true;
	}
	long long i = 2;
	long long tempNum = num;
	while (!check(digits))
	{
		num = tempNum*i;
		outDigits = getDigits(num);
		for (int i = 0; i < outDigits.size(); i++)
		{
			digits[outDigits[i]] = true;
		}
		i++;
	}
	return num;
}
int main()
{
	fstream fin;
	fstream fout;
	fin.open("A-large.in", ios::in);
	fout.open("A-large.out", ios::out);
	//fstream foutTestCase;
	//foutTestCase.open("TestCase1.in", ios::out);
	//createExtreamTestCase(foutTestCase, 424687, 1000000);
	int t;
	fin >> t;
	long long num;
	for (int i = 0; i < t; i++)
	{
		fin >> num;
		if (num == 0)
		{
			fout << "Case #" << (i + 1) << ": INSOMNIA" << endl;
		}
		else
		{
			fout << "Case #" << (i + 1) << ": "<<getLastNum(num)<< endl;
		}
	}
	return 0;
};