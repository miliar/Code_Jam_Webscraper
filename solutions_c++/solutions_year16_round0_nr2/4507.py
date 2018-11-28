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

int cntMinStep(const string& str);
int main()
{
	std::ifstream in("data.txt");
	std::streambuf *cinbuf = std::cin.rdbuf();
	std::cin.rdbuf(in.rdbuf()); 
	ofstream FILE("out.txt", ios::app);
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		string str;
		cin >> str;
		FILE << "Case #" << i + 1 << ": " <<cntMinStep(str)<< endl;
	}
	FILE.close();
	return 0;
}

int cntMinStep(const string& str)
{
	vector<char> strList;
	strList.push_back(str[0]);
	for (int i = 0; i < str.size(); i++)
	{
		if (strList[strList.size() - 1] != str[i])
			strList.push_back(str[i]);
	}

	if (strList.size() == 1)
	{
		if (strList[0] == '+')
			return 0;
		else
			return 1;
	}
	//Å¼Êý
	else if(strList.size()%2==0)
	{
		//+-+-
		if (strList[0] == '+')
		{
			return strList.size();
		}
		//-+-+
		else
		{
			return strList.size() - 1;
		}
	}
	//ÆæÊý
	else
	{
		//+-+-+
		if (strList[0] == '+')
		{
			return strList.size() - 1;
		}
		//-+-+-
		else
		{
			return strList.size();
		}
	}
}