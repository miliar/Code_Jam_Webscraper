#include <iostream>
#include <sstream>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <string>
#include <map>
#include <fstream>
#include <stdlib.h>
#include <cstdio>

using namespace std;

#define ll long long
#define pb push_back
#define fl(i, n, m)		for(int i=n; i<m; i++)
#define INT_INF 2000000000
#define LL_INF 3000000000000000000

int main()
{
	int t, n, steps;
	cin >> t;
	for(int i=0; i<t; i++)
	{
		steps = 0;
		cin >> n;
		vector<string> s(n);
		for(int j=0; j<n; j++)
			cin >> s[j];
		cout << "Case #" << i+1 << ": " ;
		int j=1, k=1;
		if(s[0][0] != s[1][0])
		{
			cout << "Fegla Won" << endl;
			continue;
		}
int flag=0;
		while(j<s[0].size() && k<s[1].size())
		{
			if(s[0][j] == s[1][k])
			{
				j++; 	k++;
				continue;
			}
			else if(s[0][j] == s[0][j-1] && s[1][k] != s[1][k-1])	s[0].erase(s[0].begin()+j);

			else if(s[1][k] == s[1][k-1] && s[0][j] != s[0][j-1])	s[1].erase(s[1].begin()+k);
			
			else
			{	cout << "Fegla Won" << endl; flag = 1; break;}

			steps++;
		}
		if(flag ==0)	{
			while(k<s[1].size())	{
				if(s[1][k] == s[0][j-1])	steps++;
				else 	{	
					cout << "Fegla Won" <<endl;
					flag = 1;
					break;
				}
				k++;
			}

			while(j<s[0].size())	{
				if(s[0][j] == s[0][k-1])	steps++;
				else	{
					cout << "Fegla Won" << endl;	flag = 1;
					break;
				}
				j++;
			}
			if(flag == 0)
			cout << steps << endl;
		}
	}
}
