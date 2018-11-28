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

void genPrimes();
vector<int> Primes;
bool isJamcoin(string str);
void allStr(int lenngth, vector<string> &strList);
int main()
{
	std::ifstream in("data.txt");
	std::streambuf *cinbuf = std::cin.rdbuf();
	std::cin.rdbuf(in.rdbuf()); 
	ofstream FILE("out.txt", ios::app);

	
	genPrimes();
	
	int Tasks;
	cin >> Tasks;
	for (int i = 0; i < Tasks; i++)
	{
		int N, J;
		cin >> N >> J;
		
		FILE << "Case #" << i + 1 << ":" << endl;

		vector<string> strList;
		allStr(N, strList);
		int cnt = 0;
		for (int i = 0;i<strList.size();i++)
		{
			if (isJamcoin(strList[i]))
			{
				
				FILE << strList[i] << " ";

				long long temp = 0;

				for (int k = 2; k <= 10; k++)
				{
					temp = 0;
					for (int j = strList[i].size() - 1; j >= 0; j--)
					{
						temp += (strList[i][j] - '0')*pow(k, strList[i].size() - 1 - j);

					}
					for (long long j = 2; j < temp; j++)
					{
						if (temp%j == 0)
						{
							FILE << j << " ";
							break;
						}
					}

				}
				FILE << endl;
				cnt++;
				if (cnt == J)
					break;
			}

		}
	}

	FILE.close();
	return 0;
}
void genPrimes()
{
	Primes.push_back(2);
	for (int i = 3; i < 100000; i++)
	{
		bool flag = false;
		for (int j = 2; j < i; j++)
		{
			if (i%j == 0)
			{
				flag = true;
				break;
			}
		}
		if (!flag)
		{
			Primes.push_back(i);
		}
	}
}
bool isJamcoin(string str)
{
	
	long long temp = 0;
	int cnt = 0;
	for (int i = 2; i <= 10; i++)
	{
		temp = 0;
		for (int j = str.size()-1; j>=0; j--)
		{
			temp += (str[j] - '0')*pow(i, str.size() - 1 - j);

		}
		for (int k = 0; k < Primes.size() && temp>Primes[k]; k++)
		{
			if (temp%Primes[k] == 0)
			{
				cnt++;
				break;
			}

		}
		
	}
	if (cnt == 9)
		return true;
	else
		return false;
}
void allStr(int lenngth, vector<string> &strList)
{
	string str(lenngth, '0');
	str[0] = '1';
	str[str.size() - 1] = '1';
	strList.push_back(str);
	for (int i = 1; i < str.size() - 1; i++)
	{
		int tempSize = strList.size();
		for (int j = 0; j < tempSize; j++)
		{
			string temp = strList[j];
			temp[i] = '1';
			strList.push_back(temp);
		}
	}
}
