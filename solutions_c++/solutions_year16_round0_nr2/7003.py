#include<stdio.h>
#include<cstring>

int solve(int n,char str[])
{
	bool isHappy[100] = {};
	for (int i = 0; i < n; i++) isHappy[i] = str[i] == '+';
	int cnt = 0;
	for (int i = n - 1; i >= 0; i--) 
	{
		if ((!isHappy[i]+cnt)%2) 
		{
			cnt++;
		}
	}
	return cnt;
}

int main()
{
	int T;
	scanf("%d", &T);
	getchar();
	for (int i = 0; i < T; i++)
	{
		char str[101];
		gets_s(str);
		int len = strlen(str);
		printf("Case #%d: %d\n", i + 1, solve(len,str));
	}
	return 0;
}