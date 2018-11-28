#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define MOD 1000000007
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
string s;

int alg()
{
	int rit;
	for(int i = s.size(); i >= 0; i--)
	{
		if(s[i] == '-'){rit = i; break;}
	}
	return rit;
}

int check()
{
	for(int i = 0; i < s.size(); i++)
	{
		if(s[i] == '-') return 0; // non piena
	}
	return 1;
}
int main()
{	
	int t;
	cin >> t;
	
	for(int i = 1; i <= t; i++)
	{
		//cout << i << endl;
		int cnt = 0,q;
		cin >> s;
		int flag = 0, a = 0;
		for(int j = 0; j < s.size()-1; j++)
		{
			if(s[i] == '-') a++;
		}
		while(!check())
		{
			cnt++;
			q = alg();
			for(int k = 0; k <= q; k++)
			{
				if(s[k] == '-') s[k] = '+';
				else s[k] = '-';
			}
		}
		printf("Case #%d: ",i);
		cout << cnt << endl;
	}
	return 0;
}