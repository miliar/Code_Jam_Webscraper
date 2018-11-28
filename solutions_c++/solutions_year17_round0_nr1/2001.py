// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string> 
#include <vector>
#include <deque>          // std::deque
#include <list>           // std::list
#include <queue>          // std::queue

using namespace std;  // since cin and cout are both in namespace std, this saves some text

string solve1(int n);
string solveTidyNumbers(string);
string solveOversizedPancakeFlipper(string s, int n);
int solve2(std::string str);

void main() {
	int t, n, m;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		//cin >> n;  // read n and then m.
		//auto res = solve1(n);

		char s[1000];
		cin >> s;
		int n = 0;
		cin >> n;

		cout << "Case #" << i << ": " << solveOversizedPancakeFlipper(s, n).c_str() << endl;
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}

string solve1(int n)
{
	bool flags[10] = {false};
	int count = 0;
	int number = 0;
	if (n == 0)
		return "INSOMNIA";
	else{
		int save = n;
		while (count < 10)
		{
			number++;
			n = save *  number;
			int f = n;
			while (f >= 1)
			{
				int d = f%10;
				f /= 10;
				if (flags[d] == false) count++;
				flags[d] = true;
			}
		}
		auto res = std::to_string(save *  number);
		return res;
	}
}

int solve2(std::string str)
{
	std::vector<bool> listHappy;
	int count = str.length();
	for (int i = 0; i < count; i++)
	{
		bool type = str[i] == '+';
		if (listHappy.size() == 0 || listHappy.at(listHappy.size() - 1) != type)
			listHappy.push_back(type);
	}
	if (count == 0) return 0;
	else
	{
		bool happyFirst = listHappy[0];
		if (happyFirst)
		{
			if (listHappy.size() == 1)
				return 0;
			else if ((listHappy.size() % 2) == 0)
				return listHappy.size();
			else
				return listHappy.size() - 1;
		}
		else
		{
			if ((listHappy.size() % 2) == 1)
				return listHappy.size();
			else
				return listHappy.size() - 1;
		}
	}
}

vector<int> listN;

void doSmallerAtPos(int pos, int value)
{


	if (value < listN[pos])
	{
		listN[pos]--;

		for (int i = pos + 1; i < listN.size(); i ++)
			listN[i] = 9;
	}

	if (pos > 0)
	{
		doSmallerAtPos(pos - 1, listN[pos]);
	}
}

void doTidyAtPos(int pos)
{
	if (pos == 0)
		return;
	else
		doSmallerAtPos(pos - 1, listN[pos]);
}


string solveTidyNumbers(string s)
{
	listN.clear();
	for (int i = 0; i < s.length(); i++)
	{
		listN.push_back(s.at(i) - '0');
	}
	doTidyAtPos(listN.size() - 1);

	bool first = true;
	string result = "";
	for (int i = 0; i < listN.size(); i++)
	{
		if (listN[i] == 0)
		{
			if (first == false)
			{
				result = result + std::to_string(0);
			}
		}
		else{
			result = result + std::to_string(listN[i]);
			first = false;
		}
	}

	return result;
}

enum type_cake{
	happy,
	empty
};

int removeHappy(std::list<type_cake> &listCake)
{
	int count = 0;
	while (listCake.size() > 0 && listCake.front() == happy)
	{
		count++;
		listCake.pop_front();
	}

	return count;
}

void flipCake(std::list<type_cake> &listCake, int n)
{
	if (listCake.size() >= n)
	{
		auto it = listCake.begin();
		int i = 0;
		while (i < n)
		{
			if (*it == happy)
				*it = empty;
			else
				*it = happy;
			i++;
			it++;
		}
	}
}

string solveOversizedPancakeFlipper(string s, int n)
{
	std::list<type_cake> listCake;
	for (int i = 0; i < s.length(); i++)
	{
		auto t = (s.at(i) == '+') ? happy : empty;
		listCake.push_back(t);
	}
	

	int count = 0;
	removeHappy(listCake);

	while (listCake.size() > 0)
	{
		flipCake(listCake, n);
		count++;
		int count1 = removeHappy(listCake);
		if (listCake.size() == 0)
			break;


		if (count1 == 0)
			return "IMPOSSIBLE";
	}

	if (listCake.size() > 0)
		return "IMPOSSIBLE";
	return to_string(count);
}