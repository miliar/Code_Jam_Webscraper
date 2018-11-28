// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include <fstream>

using namespace std;

int length(string& s)
{
	int count=0;
	char c;
	for (int i = 0; i < s.size(); i++)
	{
		if (i == 0)
		{
			c = s[0];
			count = 1;
		}
		else
		{
			if (s[i] == c);
			else
			{
				c = s[i];
				count++;
			}
		}
	}
	return count;
}

int median(vector<int>& v, int m)
{
	int cost = 0;
	for (int i = 0; i < v.size(); i++)
	{
		if (v[i] < v[m])
			cost = cost + v[m] - v[i];
		else
			cost = cost + v[i] - v[m];
	}
	return cost;
}

int cost(vector<int>& v)
{
	int cost;
	sort(v.begin(), v.end());
	if (v.size() % 2 == 1)
	{
		int m = v.size() / 2;
		cost = median(v, m);
	}
	else
	{
		int m = v.size() / 2;
		cost = median(v,m);
		int temp = median(v, m - 1);
		if (cost > temp)
			cost = temp;
	}
	return cost;
}

int cont(string& s, char& c,int& p)
{
	int count = 0;
	c = s[p];
	for (int i = p; i < s.size(); i++)
	{
		if (c == s[i]) count++;
		else
		{
			p = i;
			break;
		}
	}
	return count++;
}


bool calc(vector<string>& str,vector<int>& v,vector<int>& pos)
{
	char ch;
	for (int i = 0; i < str.size(); i++)
	{
		char c;
		v[i] = cont(str[i],c,pos[i]);
		if (i == 0) ch = c;
		else
		{
			if (ch != c)
				return false;
		}
	}
	return true;
}

int main()
{
	ofstream output;
	output.open("example.txt");
	ifstream input ("A-small-attempt0.in");
	int t,n;
	bool der = true;
	input >> t;
	for (int j = 0; j < t; j++)
	{
		der = true;
		int ans = 0;
		int max=0;
		input >> n;
		string s;
		vector<string> str;
		for (int i = 0; i < n; i++)
		{
			input >> s;
			str.push_back(s);
		}
		max = length(str[0]);
		for (int i = 1; i < n; i++)
		{
			if (max != length(str[i]))
			{
				output << "Case #" << j + 1 << ": " << "Fegla Won" << endl;
				der = false;
				break;
			}
		}
		if (der)
		{
			vector<int> pos(n);
			//cout << max << "max" << endl;
			for (int i = 0; i < max; i++)
			{
				vector<int> v(n);
				if (calc(str, v, pos))
				{
					ans = ans + cost(v);
					//cout << cost(v)<<endl;
				}
				else
				{
					ans = -1;
					break;
				}
			}

			if (ans == -1)
			{
				output << "Case #" << j + 1 << ": " << "Fegla Won" << endl;
			}
			else
			{
				output << "Case #" << j + 1 << ": " << ans << endl;
			}
		}		
	}
	input.close();
	output.close();
	//cin >> t;
	return 0;
}

