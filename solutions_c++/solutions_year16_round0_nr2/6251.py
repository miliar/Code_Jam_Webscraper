#include <bits/stdc++.h>

using namespace std;
string change(string s,int r)
{
	if(s[0]=='+')
	{
		for(int i=0 ; i<r ; i++)
		s[i]='-';
	}
	else
	{
		reverse(s.begin(),s.begin()+r+1);
		for(int i=0 ; i<=r ; i++)
		{
			if(s[i]=='+')	s[i]='-';
			else s[i]='+';
		}
	}
	return s;
}
int main()
{
	freopen("BLarge.in","r",stdin);
    freopen("Output2.out","w",stdout);
	int t;	cin >> t;
	for(int k=1 ; k<=t ; k++)
	{
		string str;	cin >> str;
		int counter=-1;
		bool check=0;
		while(!check)
		{
			counter++;
			if(str[0]=='+')
			{
				check=1;
				for(int i=1 ; i<str.size() ; i++)
				{
					if(str[i]=='-')
					{
						check=0;
						str=change(str,i);
						break;
					}
				}
			}
			else
			{
				for(int i=str.size()-1 ; i>=0 ; i--)
				{
					if(str[i]=='-')
					{
						str=change(str,i);
						break;
					}
				}
			}
		}
		cout << "Case #" << k << ": " << counter << endl;
	}
}
