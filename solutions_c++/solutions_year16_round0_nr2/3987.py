#include <bits/stdc++.h>

#define sf scanf
#define pf printf
#define ll long long int

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t = 0; t < T; t++)
	{
		string s;
		cin >> s;
		int ct = 0;
		if(s[0] == '-')
			ct++;
		for(int i = 0; i < s.size(); i++)
		{
			if(s[i] == '+')
			{
				for(i; i < s.size(); i++)
					if(s[i] == '-')
					{
						ct+= 2;
						break;
					}
				for(i; i < s.size() && s[i] == '-'; i++)
					if(s[i] == '+')
						break;
				i--;
			}
		}
		printf("Case #%d: ", t+1);
		printf("%d\n", ct);
	}
	return 0;
}
