#include <iostream>
#include <cstdio>
#include <memory.h>
#include <string>
using namespace std;

int test;
int cnt = 1;
int L, x;
char st[10001];
string dp;
string s;
int main(){
	FILE *fi = fopen("B-small-attempt3.in", "r");
	FILE *fo = fopen("output.txt", "w");

	scanf("%d", &test);

	while (test--)
	{
		s.clear();
		dp.clear();
		bool ck1 = false, ck2 = false;
		scanf("%d %d", &L, &x);
		scanf("%s", st);
		for (int i = 1; i <= x; i++)
			s.append(st), dp.append(st);
		//-i, -j ,-k´Â a, b, c.....-1Àº z
		for (int i = 1; i < s.size(); i++)
		{
			if (dp[i - 1] == '1')
				dp[i] = s[i];
			else if (dp[i - 1] == 'z')
			{
				if (s[i] == 'i') dp[i] = 'a';
				else if (s[i] == 'j') dp[i] = 'b';
				else if (s[i] == 'k') dp[i] = 'c';
			}
			else if (dp[i - 1] == 'i')
			{
				if (s[i] == 'i') dp[i] = 'z';
				else if (s[i] == 'j') dp[i] = 'k';
				else if (s[i] == 'k') dp[i] = 'b';
			}
			else if (dp[i - 1] == 'a')
			{
				if (s[i] == 'i') dp[i] = '1';
				else if (s[i] == 'j') dp[i] = 'c';
				else if (s[i] == 'k') dp[i] = 'j';
			}
			else if (dp[i - 1] == 'j')
			{
				if (s[i] == 'i') dp[i] = 'c';
				else if (s[i] == 'j') dp[i] = 'z';
				else if (s[i] == 'k') dp[i] = 'i';
			}
			else if (dp[i - 1] == 'b')
			{
				if (s[i] == 'i') dp[i] = 'k';
				else if (s[i] == 'j') dp[i] = '1';
				else if (s[i] == 'k') dp[i] = 'a';
			}
			else if (dp[i - 1] == 'k')
			{
				if (s[i] == 'i') dp[i] = 'j';
				else if (s[i] == 'j') dp[i] = 'a';
				else if (s[i] == 'k') dp[i] = 'z';
			}
			else if (dp[i - 1] == 'c')
			{
				if (s[i] == 'i') dp[i] = 'b';
				else if (s[i] == 'j') dp[i] = 'i';
				else if (s[i] == 'k') dp[i] = '1';
			}
		}

		if (dp.back() != 'z') printf("Case #%d: NO\n", cnt++);
		else
		{
			for (int i = 0; i < dp.size(); i++)
			{
				if (dp[i] == 'i') {
					ck1 = true;
				}
				if (dp[i] == 'k' && ck1)
				{
					ck2 = true;
					break;
				}
			}
			if (ck2)
				printf("Case #%d: YES\n", cnt++);
			else 
				printf("Case #%d: NO\n", cnt++);
		}
	}

}