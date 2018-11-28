// q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<string>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		long long n, cur;
		string digits("xxxxxxxxxx");
		cin >> n;
		if (n == 0){
			cout << "Case #" << i + 1 << ": INSOMNIA"<<endl;
			continue;
		}
		cur = n;
		string temp = to_string(cur);
		while (digits.compare("0123456789") != 0){
			for (int j = 0; j < temp.size(); j++)
			{
				if (temp[j] != digits[temp[j] - '0'])
					digits[temp[j] - '0'] = temp[j];
			}
			if (digits.compare("0123456789") != 0){
				cur += n;
				temp = to_string(cur);
			}
		}
		cout << "Case #" << i + 1 << ": " << cur << endl;

	}
	return 0;
}

