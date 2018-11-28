#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;

string s;
int ans,t;

int main()
{
	freopen("g2.in","r",stdin);
	freopen("g2.out","w",stdout);
	scanf("%d",&t);
	for(int k = 1; k <= t; k++)
	{
		cin >> s;
		int l = s.length();
		ans = 0;
		if(s[0] == '-')
			ans++;
		for(int i = 1; i < l; i++)
		{
			if(s[i] == '-')
			{
				if(s[i-1] == '-')
					continue;
				else
					ans += 2;
			}
		}
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}
