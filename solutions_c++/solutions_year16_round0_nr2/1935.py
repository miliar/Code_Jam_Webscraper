#include "stdafx.h"

#include <fstream>
#include <sstream>

#include <iostream>
#include <string>
#include <vector> 
#include <algorithm>
#include <map>
#include <stack>
using namespace std;

int main()
{/*
	int m = 1;
	ofstream fout;
	fout.open("output.txt");
	char res[1000002] = { 0 }; int max = 2;
	for (int n = 1; n < 1000002; n++)
	{
		//int n; 
		//cin >> n;
		int flags[10] = { 0 };
		//cout << n;
		bool flag = false;
		int i = 1;
		while (!flag)
		{
			int k = i*n;
			//cout << k << "\n";
			while (k)
			{
				flags[k % 10] = 1;
				k /= 10;
			}flag = true;
			for (int i = 0; i < 10; i++)
			{
				
				
				if (!flags[i])
				{
					flag = false;
				}
			}
			i++;
		}
		for (int i = 0; i < 10; i++)
		{
			cout << flags[i] << " ";

		}
		res[n] = (i - 1);
		fout << (i - 1) << ", ";
		cout << n << " " << ((i - 1)*n) << " " << (i-1) << "\n";
		max = (i - 1) > max ? (i - 1) : max;
	}
	cout << max;
	fout.close();
	cin >> m;*/

	int t;
	string input = "";
	ifstream fin;
	ofstream fout;
	fin.open("bsm.in");
	fout.open("outp.out");
	getline(fin, input);
	stringstream myStream(input);
	myStream >> t;
	for (int i = 0; i < t; i++)
	{
		stack<char> mystack;
		getline(fin, input);
		for (int i = 0; i < input.length(); i++)
		{
			mystack.push(input[i]);
		}
		int flip = 0;
		while (!mystack.empty())
		{
			char cur = mystack.top();
			if ((cur == '+' && (flip % 2) == 1) || (cur == '-' && (flip % 2) == 0))
			{
				flip++; 
			}
			mystack.pop();
		}
		fout << "Case #"<<(i+1)<<": " << flip << "\n";
	}
}