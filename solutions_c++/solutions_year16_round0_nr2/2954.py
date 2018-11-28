#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<bitset>
using namespace std;
#define mem(x) memset(x,0,sizeof x)
#define LL long long

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin.tie(NULL);
	int t; cin >> t;
	for (int kcase = 1; kcase <= t; kcase++)
	{
		string s = "";
		cin >> s;
		int ans = 0;
		int i = 0;
		
		char temp = s[0];
		while (i < s.length())
			{
				if (temp == '+')
				{
					if (s[i] == '-'){ ans++; temp = '-'; }
					else i++;
				}
				else if (temp == '-')
				{
					if (s[i] == '+'){ ans++; temp = '+'; }
					else i++;
				}
			}
			if (temp == '-') ans++;
		
	
		printf("Case #%d: %d\n", kcase, ans);
	}
	return 0;
}