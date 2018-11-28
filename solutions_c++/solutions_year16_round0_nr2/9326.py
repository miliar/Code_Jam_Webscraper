#include <bits/stdc++.h>

using namespace std;

string convert(string str)
{
	for (int i=0;i<str.length();i++)
	{
		str[i] = str[i]=='-'?'+':'-';
	}
	return str;
}

int ans(string str)
{
	int cnt = 0;
	for (int i=str.length()-1;str[i] == '+'&&i>=0;i--)
	{
		cnt ++;
	}
	str = str.substr(0, str.length()-cnt);
	if (str.length() == 0)
		return 0;
	cnt = 0;
	for (int i=0;i<str.length()&&str[i] == '+';i++)
	{
		cnt ++;
	}
	int ret = 0;
	if(cnt > 0)
	{
		ret ++;
		for (int i=0;i<cnt;i++)
		{
			str[i] = '-';
		}
	}
	cnt = 0;
	for (int i=0;i<str.length()&&str[i] == '-';i++)
	{
		cnt ++;
	}
	string left = str.substr(cnt);
	reverse(left.begin(), left.end());
	left = convert(left);
	return ret + 1 + ans(left);
}

int main()
{
	int T;
	cin>>T;
	for (int t=0;t<T;t++)
	{
		string pans;
		cin>>pans;
		printf("Case #%d: %d\n", t+1, ans(pans));
	}
	return 0;
}