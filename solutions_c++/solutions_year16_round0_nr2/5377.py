#include <bits/stdc++.h>
using namespace std;


void solve(int C)
{
	int cnt = 0, i, len, ans = 0;
	string s;
	bool flag;

	cin>>s;

	len = s.length();

	i = 0;
	if(s[0] == '+')
		i = 0;	
	else
	{
		while(s[i] == '-')
			i++;
		ans += 1;
	}

	for(i ; i < len ; i++)
	{
		if(s[i] == '+')
			flag = true;
		else if(flag == true)
		{
			cnt++;
			flag = false;
		}
		else
			continue;
	}

		ans += 2*cnt;

	printf("Case #%d: %d\n", C,ans );
	return;
}

int main()
{
	int t;
	scanf("%d", &t);

	for(int i = 0 ; i < t ; i++)
		solve(i+1);
	return 0;
}