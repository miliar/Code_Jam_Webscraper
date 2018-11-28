#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <bitset>
#include <utility>
#include <fstream>
#include <iostream>
#include <limits>

#define MAX_N 16

using namespace std;

vector<vector<string>> result;
map<__int64, __int64> hashmap;

__int64 getDivisor(__int64 num)
{
	if (num == 1) return 0;
	__int64 temp = sqrt(num);
	for (__int64 i = 2; i <= temp; i++)
	{
		if (num%i == 0) return i;
	}
	return 0;
}

int main()
{
	ifstream inputfile;
	ofstream outputfile;

	// char *inputfilename = argv[2];
	inputfile.open("C-small-attempt1.in");
	// inputfile.open(inputfilename);
	outputfile.open("output.txt");
	outputfile.clear();

	int cases;
	// int count = 1;
	// input case number
	inputfile >> cases;

	// m different jamcoins of length n
	int n, m;

	//n = MAX_N;
	//vector<string> coinjams;
	//// n = 0, 1, 2 no coinjams
	//result.push_back(coinjams);
	//result.push_back(coinjams);
	//result.push_back(coinjams);

	//for (int i = 3; i <= n; i++)
	//{
	//	int mid = pow(2, i - 2);
	//	coinjams.clear();
	//	for (int digit = 0; digit < mid; digit++)
	//	{
	//		string binary = "";
	//		int temp = digit;
	//		// cout << digit << ":	";
	//		for (int d = 1; d <= i-2; d++)
	//		{
	//			if (temp & 1) binary = '1' + binary;
	//			else binary = '0' + binary;
	//			temp >>= 1;
	//		}
	//		binary = '1' + binary + '1';
	//		// cout << binary << endl;

	//		bool valid = true;
	//		for (int base = 2; base < 11 && valid; base++)
	//		{
	//			__int64 basic = 1;
	//			__int64 number = 0;
	//			for (int index = i - 1; index >= 0; index--)
	//			{
	//				number += (binary[index] - '0') * basic;
	//				basic *= base;
	//			}
	//			if (getDivisor(number) == 0) valid = false;
	//		}
	//		if (valid) coinjams.push_back(binary);
	//	}
	//	result.push_back(coinjams);
	//}

	inputfile >> n >> m;
	outputfile << "Case #1:" << endl;

	int count = 0;
	vector<__int64> divisors;
	
	int variation = pow(2, n - 2);
	for (int mid = 0; mid < variation && count != m; mid++)
	{
		string binary = "";
		int temp = mid;
		// cout << digit << ":	";
		for (int d = 1; d <= n - 2; d++)
		{
			if (temp & 1) binary = '1' + binary;
			else binary = '0' + binary;
			temp >>= 1;
		}
		binary = '1' + binary + '1';
		// cout << binary << endl;

		bool valid = true;
		divisors.clear();
		for (int base = 2; base < 11 && valid; base++)
		{
			__int64 multiple = 1;
			__int64 number = 0;
			for (int index = n - 1; index >= 0; index--)
			{
				number += (binary[index] - '0') * multiple;
				multiple *= base;
			}
			__int64 div = getDivisor(number);
			if (div == 0) valid = false;
			else
			{
				divisors.push_back(div);
			}
		}
		// output binary and divisors
		if (valid)
		{
			count++;
			outputfile << binary;
			for (int x = 0; x < 9; x++)
				outputfile << " " << divisors[x];
			outputfile << endl;
		}
	}

	// system("pause");
	return 0;
}