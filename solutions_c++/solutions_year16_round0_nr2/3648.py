#include <bits/stdc++.h>
using namespace std;
#define ll long long int

int calculate(string s)
{
	int k=0;
	int count = 0;
	while(k < s.length())
	{
		char p = s.at(k);
		while(k < s.length() && s.at(k) == p)
		{
			k++;
		}
		count++;
	}
	return count;
}

int main()
{
	ll n, i, j, t;
	cin >> t;
	for(i=0; i<t; i++)
	{
		string s;
		ll count = 0;		
		cin >> s;
		if(s.compare("-") == 0)
		{
			cout << "Case #"<< (i+1) <<": "<< 1 <<'\n';
		}
		else if(s.compare("+") == 0)
		{
			cout << "Case #"<< (i+1) <<": "<< 0 <<'\n';
		}
		else
		{
			char start = s.at(0);
			char end = s.at(s.length()-1);
			if(start == '+' && end == '-')
			{
				cout << "Case #"<< (i+1) <<": "<< calculate(s) <<'\n';
			}
			else if(start == '+' && end == '+')
			{
				cout << "Case #"<< (i+1) <<": "<< calculate(s)-1 <<'\n';
			}
			else if(start == '-' && end == '+')
			{
				cout << "Case #"<< (i+1) <<": "<< calculate(s)-1 <<'\n';
			}
			else
			{
				cout << "Case #"<< (i+1) <<": "<< calculate(s) <<'\n';
			}
		}
	}
}

