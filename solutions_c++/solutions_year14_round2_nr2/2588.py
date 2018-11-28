#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	freopen("aain.txt", "r", stdin);
	freopen("aaout.txt", "w", stdout);
	int tc, a, b, k;
	scanf("%d", &tc);
	int ctr=0, t=0;
	while(tc--)
	{
		t++;
		ctr=0;
		scanf("%d%d%d", &a, &b, &k);
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if((i&j)<k)
				ctr++;
			}
		}
		printf("Case #%d: ", t);
		printf("%d\n", ctr);
	}
}

