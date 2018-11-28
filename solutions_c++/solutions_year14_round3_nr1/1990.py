// coder.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"

#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include <fstream>
#include<regex>

using namespace std;

void numb(string& s,int& p,int& q)
{
	p = 0; q = 0;
	int i;
	for (i = 0; i < s.size(); i++)
	{
		if (s[i] == '/')
			break;
		p = p * 10 + s[i] - '0';
	}
	i++;
	for (; i < s.size(); i++)
	{
		q = q * 10 + s[i] - '0';
	}
}

int gcd(int a, int b)
{
	if (a == 0) return b;
	return gcd(b%a, a);
}

bool check(int& p, int& q)
{
	int temp = gcd(p, q);
	p = p / temp;
	q = q / temp;
	int count = 0;
	int qt = q;
	while (1)
	{
		if (qt == 1) break;
		if (qt % 2 == 1)
			return false;
		qt = qt / 2;
		count++;
	}
	if (p <= pow(2, count))
	{
		q = count;
		return true;
	}
		
	return false;
}

int powr(int p)
{
	int temp = 1;
	int count = 0;
	if (p == 1)
		return 0;
	while (1)
	{
		if (p <= temp)
		{
			return --count;
		}
		temp = 2 * temp;
		count++;
	}
}

int main()
{
	ofstream output;
	output.open("ouput.txt");
	ifstream input("A-small-attempt0.in");
	int t;
	input >> t;
	for (int c = 0; c < t; c++)
	{
		string s;
		int p, q;
		input >> s;
		numb(s,p,q);
		if (check(p, q))
		{
			int val = powr(p);
			output << "Case #" << c + 1 << ": " << q-val << endl;
		}
		else
		{
			output << "Case #" << c + 1 << ": " << "impossible" << endl;
		}
	}
	input.close();
	output.close();
	return 0;
}

