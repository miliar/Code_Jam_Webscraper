//============================================================================
// Name        : pancake.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.out", "w", stdout);


	char s[101];
	int t, nt;
	int prev;
	int changes;

	cin>>t;

	for(nt = 0; nt<t; nt++)
	{
		cin>>s;

		changes = 0;
		for(int i=0; i<strlen(s); i++)
		{
			if(i==0)
			{
				if(s[i] == '+')
				{
					prev = 0;
				}
				else if(s[i] == '-')
				{
					prev = 1;
				}

			}
			else
			{
				if(s[i] == '+')
				{
					if(prev == 1)
					{
						changes++;
						prev = 0;
					}
				}
				else
				{
					if(prev == 0)
					{
						changes++;
						prev = 1;
					}
				}
			}
		}

		if(prev == 1)
		{
			cout<<"Case #"<<nt+1<<": "<<changes+1<<endl;
		}
		else
		{
			cout<<"Case #"<<nt+1<<": "<<changes<<endl;
		}
	}









	return 0;
}
