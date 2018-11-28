#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for (int k = 1; k <= t; ++k)
	{
		string s;
		cin>>s;
		string compa = "";
		for(int i = 0 ; i < s.size(); i ++)
		{
			if(s[i] == '+')
			{
				s[i] = '1';
			}
			else
			{
				s[i] = '0';
			}
			compa+='1';
		}
		int cont = 0;
		while(s!=compa)
		{
			int j = 0;
			while(s[j] == s[j+1] && j<s.size())
			{
				j++;
			}
			for(int i = 0 ; i <= j; i ++)
			{
				if(s[i]=='1')
				{
					s[i]='0';
				}
				else
				{
					s[i] = '1';
				}
			}
			cont++;
		}
		cout<<"Case #"<<k<<": "<<cont<<endl;
	}
	return 0;
}