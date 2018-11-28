// hihoLV1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <list>
#include <map>
using namespace std;
void cntSleep(long long startNum, int index);
bool check(const map<int, bool>& digits);
int main()
{
	std::ifstream in("data.txt");
	std::streambuf *cinbuf = std::cin.rdbuf();
	std::cin.rdbuf(in.rdbuf()); 


	int  N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		long long temp;
		cin >> temp;
		cntSleep(temp, i);
	}
	return 0;
}
void cntSleep(long long startNum,int index)
{
	ofstream FILE("out.txt",ios::app);
	map<int, bool> digits;
	for (int i = 0; i < 10; i++)
	{
		digits[i] = false;
	}
	for (int i = 1; i < 100; i++)
	{
		long long num = i*startNum;
		string str = to_string(num);
		for (int i = 0; i < str.size(); i++)
		{
			digits[str[i] - '0'] = true;
		}
		if (check(digits))
		{
			FILE << "Case #" << index + 1 << ": " << num << endl;
			FILE.close();
			return;
		}
	}
	FILE << "Case #" << index + 1 << ": INSOMNIA" << endl;
	FILE.close();
	return ;
}
bool check(const map<int, bool>& digits)
{
	for (int i = 0; i < 10; i++)
	{
		auto it = digits.find(i);
		if ((*it).second==false)
			return false;
	}
	return true;
}