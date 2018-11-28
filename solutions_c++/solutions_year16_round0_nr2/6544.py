/*
https://code.google.com/codejam/contest/6254486/dashboard#s=p1
*/

#include<iostream>
#include<algorithm>
#include<string>
#include<cstdio>

using namespace std;

int main()
{
	int tc;
	cin >> tc;

	for(int cases=1;cases<=tc;cases++)
	{
		string str;
		cin >> str;
		int l = str.length();

		int st = 0;
		int i  = 0;
		int ans= 0;
		int flag = 0;

		while(i<=l)
		{
			if(i==l)
			{
				if(1==flag) ans = ans + (0==st?1:2);
			}
			else
			{
				if(str[i] == '-')
				{
					if(0==i) st = i;
					else if(i>0 && str[i-1]!='-') st = i;
					flag = 1;
				}
				else
				{
					if(1==flag) ans = ans + (0==st?1:2);
					flag = 0;
				}
			}
			i++;
		}
		cout << "Case #" << cases << ": " << ans << endl;
	}
}
