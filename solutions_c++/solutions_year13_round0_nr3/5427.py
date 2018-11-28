#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int len_num(int num)
{
	int l = 0;
	while(num>0)
	{
		l++;
		num /= 10;
	}
	return l;
}

int rev(int num)
{
	int ans = 0;
	while(num>0)
	{
		ans += (num%10*pow(10,len_num(num)-1));
		num /= 10;
	}
	return ans;
}

bool ispal(int num)
{
	return num==rev(num);
}

bool isint(double num)
{
	if(num - int(num) <= 0.000000001)
	return true;
	else
	return false;
}

bool fair(int number)
{
	if(ispal(number)==true and ispal(sqrt(double(number)))==true and isint(sqrt(double(number)))==true)
	return true;
	else
	return false;
}

int range(int a, int b)
{
	int left = 0;
	int right = 0;
	for(int i = 1; i < a; i++)
	{
		if(fair(i)==true)
		left++;
	}
	for(int i = 1; i <= b; i++)
	{
		if(fair(i)==true)
		right++;
	}
	return right-left;
}

int main()
{
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		int l,r;
		cin >> l >> r;
		cout << "Case #" << i+1 << ": " << range(l,r) << endl;
	}
	return 0;
}

