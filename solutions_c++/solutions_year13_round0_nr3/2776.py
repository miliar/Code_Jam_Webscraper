// main project file.

#include "stdafx.h"
#include <assert.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <algorithm>
using namespace std;
using namespace System;
int myatoi(char c)
{
	return ((int)c) - 48;
}
int fullCount(int size)
{
	// if whole group included (length n): 
	// 2: 1 + (n % 2 == 1 && n > 1)
	// 121: (n >= 3 && n % 2 == 1) * ((n-3)/2 + 1)
	// (n % 2 == 0)*(1 + a + a(a-1)/2 + a(a-1)(a-2)/6) [a = (n-2)/2]
	// (n % 2 == 1)*(1 + (n >= 3))*(1 + a + a(a-1)/2 + a(a-1)(a-2)/6) [a = (n-3)/2, min 0]

	int ans = 1;
	int free = (size-2)/2;
	if(free < 0)
		free = 0;
	if(size % 2 == 1)
		ans++;
	int mult = 1;
	if(size >= 3 && size % 2 == 1)
	{
		ans += (free + 1);
		mult = 2;
	}
	ans += (1 + free + (free*(free-1))/2 + (free*(free-1)*(free-2))/6)*mult;
	return ans;
}
bool nextPerm(vector<int> s)
{
	int count = 0;
	int place = 0;
	for(int i = 0; i < s.size(); i++)
	{
		if(s[i] == 1)
		{
			count++;
			place = i;
		}
	}
	if(count == 0)
		return false;
	s[place] = 0;
	for(int i = place+1; i < s.size() && i < place+5-count; i++)
		s[i] = 1;
	return true;
}
int gen(int p, vector<int> key, bool odd, int extra)
{
	if(p == 0)
		return 1;
	p--;
	if(p < key.size())
		return key[p];
	p -= key.size();
	if(p == 0 && odd)
		return 2 - extra;
	if(p < key.size())
		return key[key.size() - 1 - p];
	return 1;
}
int square_and_compare(vector<int> s, vector<int> key, bool include, bool odd)
{
	int ans = 0;
	int len = 2 + key.size()*2 + (odd ? 1 : 0);
	
	for(int i = 0; i < (odd ? 3 : 1); i++)
	{
		vector<int> square(s.size(), 0);
		for(int j = 0; j < len; j++)
		{
			for(int k = 0; k < len; k++)
			{
				int a = gen(j, key, odd, i);
				int b = gen(k, key, odd, i);
				square[i+j] += a*b;
			}
		}
		if(square > s)
			ans++;
		if(square == s && include)
			ans++;
	}

	return ans;
}
int overCount(vector<int> s, int n, bool include)
{
	int ans = 0;
	int digits = n*2 - 1;
	if(s.size() > digits)
		return 0;
	if(s.size() < digits)
		return fullCount(n);
	if(s[0] > 4)
		return (n == 1 && (s[0] < 9 || include)) ? 1 : 0;
	else if(s[0] < 4)
		ans += (n%2 == 1) ? 2 : 1;
	else
	{
		if(n == 1)
			return include ? 2 : 1;
		vector<int> comp(s.size(), 0);
		comp[0] = 4;
		comp[comp.size()-1] = 4;
		comp[comp.size()/2] = 8;
		if(s < comp)
			return (n%2 == 1) ? 2 : 1;
		if(s == comp)
			return (n%2 == 1 ? 1 : 0) + (include ? 1 : 0);
		if(n%2 == 0)
			return 0;
		comp[comp.size()/2] = 9;
		comp[comp.size()/4] = 4;
		comp[comp.size()/2 + comp.size()/4] = 4;
		if(s < comp)
			return 1;
		if(s > comp)
			return 0;
		return (include ? 1 : 0);
	}

	if(s[0] > 1)
	{
		return ans;
	}
	if(n == 1)
		return ans + (include ? 1 : 0);
	if(n == 2)
	{
		vector<int> v(3, 1);
		v[1] = 2;
		return ans + ((s < v || (s == v && include)) ? 1 : 0);
	}
	vector<int> key((n-2)/2, 0);
	for(int i = 0; i < key.size() && i < 3; i++)
		key[i] = 1;
	while(nextPerm(key))
		ans += square_and_compare(s, key, include, n%1 == 1);
	return ans;
}
int underCount(vector<int> s, int n)
{
	return fullCount(n) - overCount(s, n, false);
}

int main(array<System::String ^> ^args)
{

	string file;
	string path = "C:\\Users\\Ben\\Downloads\\";
	int problemNum = 0;
	cin >> problemNum;
	getline (cin,file);
    ifstream infile;
	ofstream outfile;
	infile.open (path + file + ".in");
	outfile.open (file + ".out");
	if(problemNum == 0) // example for io. sums a list of numbers.
	{
		vector<int> output;
		int size1;
		int size2;
		int val;
		infile >> size1;
		for(int i = 0; i < size1; i++)
		{
			output.push_back(0);
			infile >> size2;
			for(int j = 0; j < size2; j++)
			{
				infile >> val;
				output[i] += val;
			}
			outfile << output[i] << endl;
		}


	}
	if(problemNum == 1)
	{
		int size1;
		infile >> size1;
		for(int i = 0; i < size1; i++)
		{
			char down[] = {' ',' ',' ',' '};
			char diag[] = {' ',' '};
			string ln;
			char status = '.';
			bool filled = true;
			for(int j = 0; j < 4; j++)
			{
				infile >> ln;
				char first = ln[0];
				if(first == 'T')
					first = ln[1];
				bool good = true;
				for(int k = 0; k < 4; k++)
				{
					if(ln[k] != first && ln[k] != 'T')
						good = false;
					if(ln[k] == '.')
						filled = false;
					if(down[k] == ' ')
						down[k] = ln[k];
					else
					{
						if(down[k] == 'T')
							down[k] = ln[k];
						if(down[k] != ln[k] && ln[k] != 'T')
							down[k] = '-';
					}
					if(k == j)
					{
						if(diag[0] == ' ')
							diag[0] = ln[k];
						else
						{
							if(diag[0] == 'T')
								diag[0] = ln[k];
							if(diag[0] != ln[k] && ln[k] != 'T')
								diag[0] = '-';
						}
					}
					if(k == 3-j)
					{
						if(diag[1] == ' ')
							diag[1] = ln[k];
						else
						{
							if(diag[1] == 'T')
								diag[1] = ln[k];
							if(diag[1] != ln[k] && ln[k] != 'T')
								diag[1] = '-';
						}
					}
				}
				if(good && (first == 'X' || first == 'O'))
					status = first;
			}
			for(int j = 0; j < 4; j++)
				if(down[j] == 'X' || down[j] == 'O')
					status = down[j];
			for(int j = 0; j < 2; j++)
				if(diag[j] == 'X' || diag[j] == 'O')
					status = diag[j];
			if(status == 'X' || status == 'O')
			{
				outfile << "Case #" << i+1 << ": " << status << " won" << endl;
			}
			else if(filled)
			{
				outfile << "Case #" << i+1 << ": Draw" << endl;
			}
			else
			{
				outfile << "Case #" << i+1 << ": Game has not completed" << endl;
			}
		}
	}
	if(problemNum == 2)
	{
		int size1;
		infile >> size1;
		for(int i = 0; i < size1; i++)
		{
			outfile << "Case #" << i+1 << ": ";
		}
	}
	if(problemNum == 3)
	{
		// first digit 3+: not possible
		// first digit 2: either all 0's (till last digit) or one 1 in the middle.
		// first digit 1: middle digit 2 and up to one 1 somewhere else, or middle digit 0 or 1 and up to three 1's somewhere else.

		// if whole group included (length n): 
		// 2: 1 + (n % 2 == 1 && n > 1)
		// 121: (n >= 3 && n % 2 == 1) * ((n-3)/2 + 1)
		// (n % 2 == 0)*(1 + a + a(a-1)/2 + a(a-1)(a-2)/6) [a = (n-2)/2]
		// (n % 2 == 1)*(1 + (n >= 3))*(1 + a + a(a-1)/2 + a(a-1)(a-2)/6) [a = (n-3)/2, min 0]
		int size1;
		infile >> size1;
		for(int i = 0; i < size1; i++)
		{
			string lower;
			string upper;
			infile >> lower >> upper;
			int l = lower.length();
			int u = upper.length();
			vector<int> lowerV(l, 0);
			vector<int> upperV(u, 0);
			for(int j = 0; j < l; j++)
				lowerV[j] = myatoi(lower[j]);
			for(int j = 0; j < u; j++)
				upperV[j] = myatoi(upper[j]);
			int minFull = (l+1)/2 + 1;
			int maxFull = u/2;
			int answer = 0;
			bool under = false;
			if(u % 2 == 1 && upperV[0] > 4 && u > 1)
				maxFull++;
			else if(u % 2 == 1)
			{
				answer += underCount(upperV, maxFull + 1);
				under = true;
			}
			for(int j = minFull; j <= maxFull; j++)
				answer += fullCount(j);
			if(l % 2 == 1)
			{
				answer += overCount(lowerV, minFull - 1, true);
				if(under && minFull - 1 == maxFull + 1)
					answer -= fullCount(minFull - 1);
			}
			
			outfile << "Case #" << i+1 << ": " << answer << endl;
		}
	}
	if(problemNum == 4)
	{
		int size1;
		infile >> size1;
		for(int i = 0; i < size1; i++)
		{
			int startKeys;
			int chestCount;
			infile >> startKeys >> chestCount;
			map<int, int> keys;
			list<int> queue;
			int key;
			for(int j = 0; j < startKeys; j++)
			{
				infile >> key;
				
				queue.push_back(key);
			}
			set<int> unopened;
			map<int, pair<int, vector<int> > > chests;
			for(int j = 0; j < chestCount; j++)
			{
				int keyCount;
				infile >> key;
				infile >> keyCount;
				unopened.insert(key);
				for(int k = 0; k < keyCount; k++)
				{
					int key2;
					infile >> key2;
					chests[key].second.push_back(key2);
				}
				chests[key].first++;
			}

			while(queue.size() > 0)
			{
				int next = queue.front();
				queue.pop_front();
				keys[next]++;
				if(unopened.count(next) == 0)
					continue;
				unopened.erase(next);
				keys[next] -= chests[next].first;
				for(int j = 0; j < chests[next].second.size(); j++)
				{
					queue.push_back(chests[next].second[j]);
				}
			}

			outfile << "Case #" << i+1 << ": ";
		}
	}
	infile.close();
	outfile.close();
    return 0;
}
