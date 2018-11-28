// Q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <vector>

using namespace std;

long int need_number(int Smax, string S_str)
{
	int i;
	long int sum=0;
	long int need_total=0;
	long int need_this=0;

	if (Smax==0)
		return need_total;
	else
		for (i=0;i<(Smax+1);i++)
		{
			char num_char=S_str[i];
			int num=num_char-48;
			if (i==0)
			{
				sum=num;
				continue;
			}
			if (num==0)
				continue;
			if (i>sum)
			{
				need_this=i-sum;
				need_total=need_this+need_total;
				sum=sum+num+need_this;
			}
			else
				sum=sum+num;
		}


	return need_total;
}






int main()
{
    freopen("C://wxy_project//A-large.in", "r", stdin);
    freopen("C://wxy_project//A-large.out", "w", stdout);

	int Casenum;
	cin >> Casenum;

	for(int i=0; i<Casenum; i++) {
		int Smax;
		string S_str;
		cin>>Smax>>S_str;

		cout << "Case #" << (i+1) << ": " << need_number(Smax, S_str) << endl;
	}
	return 0;
}

