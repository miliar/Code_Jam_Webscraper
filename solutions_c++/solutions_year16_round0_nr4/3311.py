#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for (int tc = 1; tc <= t; ++tc)
	{
		int a,b,c;
		scanf("%d %d %d",&a,&b,&c);
		printf("Case #%d: ", tc);
		for (int i = 1; i < c; ++i)
		{
			printf("%d ", i);
		}
		printf("%d\n", c);
	}
	return 0;
}