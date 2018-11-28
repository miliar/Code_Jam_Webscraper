#include <iostream>
using namespace std;
int nums[2500];
int solve(char s[100])
{
	int len, tot = 0;
	for (len = 0; s[len] != '\0'; len++);
	if (len == 1)
	{
		if (s[0] == '+')
			tot = 0;
		else
			tot = 1;
	}
	else
	{
		if (s[len-1] == '+')
		{
			s[len-1] = '\0';
			len--;
			tot = solve(s);
		}
		else
		{
			s[len-1] = '\0';
			len--;
			for (int i = 0; i < len; i++)
			{
				if (s[i] == '+')
					s[i] = '-';
				else
					s[i] = '+';
			} 
			tot = 1 + solve(s);
		}
	}
	return tot;
}
int main()
{
	int t, tot;
	cin>>t;
	for (int i = 1; i <= t; i++)
	{
		char s[100];
		cin>>s;
		tot = solve(s);
		cout<<"Case #"<<i<<": "<<tot<<endl;
	}
}
