#include <iostream>
#include <cstdio>
using namespace std;

char s[10000];
int n;

int solve()
{
	scanf("%d", &n);

	scanf("%s", s);

	int i, res = 0;
	int temp = 0;
	for(i = 0; i <= n; i++)
	{
		if(temp < i)
		{
			res += i - temp;
			temp = i;
		}

		temp += s[i] - '0';
	}

	return res;
}
int main ()
{

	int t; 
	scanf ("%d", &t);

	for(int i = 1; i <= t; i++)
	{
		printf("Case #%d: %d\n", i, solve());
	}

	return 0;
}