#pragma warning(disable : 4996)
#include <stdio.h>
#include <iostream>
#include <set>

using namespace std;

void process(int t)
{
	printf("Case #%d: ", t + 1);
	char s[1000];
	scanf("%s", s);
	int res = 0;
	int l = strlen(s);
	for (int i = 1; i < l; i++)
		if (s[i] != s[i - 1])
			res++;
	if (s[l - 1] == '-')
		res++;
	printf("%d", res);
	printf("\n");
}

int main()
{
	freopen("d:\\acm\\CodeJam\\2016\\CodeJamQual\\B\\B.in", "r", stdin);
	freopen("d:\\acm\\CodeJam\\2016\\CodeJamQual\\B\\B.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		process(t);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}