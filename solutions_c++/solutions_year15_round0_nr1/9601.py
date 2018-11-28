#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	int t;
	scanf("%d", &t);
	int cs = 1;
	while (t--)
	{
		int maxS;
		scanf("%d", &maxS); 
		getchar();
		int curr = 0;
		int ans = 0;
		for (int i = 0; i <= maxS; ++i)
		{
			char ctmp;
			scanf("%c", &ctmp);
			ctmp -= '0';
			int tmp = ctmp;
			if (curr >= i)
			{
				curr += tmp;
			}
			else
			{
				ans += (i - curr);
				curr += ((i - curr) + tmp);
			}
		}
		printf("Case #%d: %d\n", cs,ans);
		cs++;
	}
}