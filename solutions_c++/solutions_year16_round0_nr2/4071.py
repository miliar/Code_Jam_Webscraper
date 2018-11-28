/*
 * pancakes.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: natali
 */
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	cin>>T;
	long long count;
	string s;
	char a;
	for(int t=1; t<=T; t++)
	{
		count=0;
		cin>>s;
		a=s[0];
		for(int i=1; i<s.size(); i++)
		{
			if(s[i]!=a)
			{
				count++;
				a=s[i];
			}
		}
		if(a=='-') count++;
		cout<<"Case #"<<t<<": "<<count<<endl;
	}
	return 0;
}


