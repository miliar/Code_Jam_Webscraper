#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main()
{
	int t;
	scanf(" %d", &t);
	for(int tt = 1; tt <= t; tt++)
	{
		int s;
		scanf(" %d", &s);
		char w[s + 10];
		scanf(" %s", &w);
		int ct = 0, k = 0;
		for(int i = 0; i <= s; i++)
		{
			if(ct < i)
			{
				k += i - ct;
				ct += i - ct;
			}
			ct += w[i] - '0';
		}
		printf("Case #%d: %d\n", tt, k);
	}
	return 0;
}

