
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, n,cas=1;
	char a[2000];
	scanf("%d", &t);

	while (t--)
	{
		scanf("%d %s",&n,a);
		int sum = 0, k = 0;
		for (int i = 0; i < n + 1; i++)
		{
			sum += a[i]-'0';
			if (sum < i + 1)
			{
				sum++; k++;
			}
			

		}
		printf("Case #%d: %d\n",cas++, k);

	}
	return 0;

}