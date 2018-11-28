/*
 * Problem C. Fair and Square.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: sara
 */

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <utility>
#include <vector>

using namespace std;

string toString(int num)
{
	string res = "";
	int i = 10;

	if (num == 0)
		return "0";
	while(num != 0)
	{
		int rem = num%i;
		res = (char)(rem + '0') + res;
		num /= i;
	}

	return res;
}

int toInt(string num)
{
	int res = 0;
	int mult = 1;
	for(int i = num.length() - 1; i >= 0; i--)
	{
		res += (num[i] - '0')*mult;
		mult*=10;
	}

	return res;
}

bool isPalin(string s)
{
	for(int i = 0 ; i < s.length()/2 ; i++)
		if(s[i] != s[s.length() - i -1])
			return false;

	return true;
}

int calc (string palin, int beg, int end)
{
	int num, sqnum;
	if((num = toInt(palin)) > end)
		return 0;

	int c = 0;
	sqnum = sqrt(num);
	if(num >= beg  && (int)sqnum * (int)sqnum == num && isPalin(toString(sqnum)))
	{
//		cout<<"num : " <<toInt(palin) << "root : " << sqnum <<endl;
		c ++;
	}

//	cout<<palin<<endl;
	for(int i = 0; i < 10 ; i++)
	{
		if(palin.empty() && i == 0) continue;
		string cur = palin.substr(0, palin.length()/2) + toString(i) +
									palin.substr(palin.length()/2);
//		cout<<cur<<endl;
		num = toInt(cur);
		sqnum = sqrt(num);
		if(num <= end && num >= beg &&  (int)sqnum * (int)sqnum == num
				 && isPalin(toString(sqnum)))
		{
//			cout<<"num  in : " <<toInt(cur) << "root : " << sqnum <<endl;
			c ++;
		}

		cur = palin.substr(0, palin.length()/2) + toString(i) + toString(i) +
							palin.substr(palin.length()/2);
//		cout<<cur<<endl;
		c += calc(cur, beg, end);
	}

	return c;
}
int main()
{

	freopen("C-small-attempt0.in", "rt", stdin);
		freopen("C-small-attempt0.out", "wt", stdout);
	int t, a, b;
	scanf("%d", &t);

	int c = 1;
	while(c <= t)
	{
		scanf("%d%d", &a, &b);
		int count = 0;

		count += calc("", a, b);
		printf("Case #%d: %d\n", c, count);
		c++;
	}
	return 0;
}	
	













