#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
int t;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output4.out", "w", stdout);
	int count = 0;
	
	cin >> t;
	while(t--)
	{
		int i, m = 0;
		char s[110];
		
		cin >> s;
		int l = strlen(s);
		s[m++] = s[0];
		for(i = 1; i < l; i++)
			if(s[i] != s[i-1])
				s[m++] = s[i];
		long long sum = 0;
		for(i = 0; i < m; i++)
		{
			if(i == 0 && s[i] == '-')
				sum++;
			else
			{
				if(s[i] == '-')
					sum += 2;
			}
		}
		printf("Case #%d: %lld\n", ++count, sum);
	}
	return 0;
}
