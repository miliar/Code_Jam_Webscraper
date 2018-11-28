#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<string.h>
#include<vector>
using namespace std;
const int N = 1000 + 5;

int main()
{
	int T;
	scanf("%d", &T);
	int p = 1;
	while(T--)
	{
		int res = 0;
		int people = 0;
		int n;
		char s[N];
		scanf("%d %s", &n, s);
		people += (int)(s[0] - '0');
		for(int i = 1; i <= n; i++)
		{
			if(people >= i)
			{
				people += (int)(s[i] - '0');
			}
			else
			{
				int add = i - people;
				people += (int)(s[i] - '0') + add;
				res += add;
			}
		}
		printf("Case #%d: %d\n", p++, res);
	}
}