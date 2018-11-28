#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	char a[1004];
	int i, t, n, tt = 1, avail, miss;
	scanf("%d", &t);
	while(t--)
	{
		avail = miss = 0;
		scanf("%d", &n);
		scanf("%s", a);
		for(i = 0; i <= n; i++)
		{
			if(avail < i && a[i] != '0')
			{
				miss += i-avail;
				avail += i-avail;
			}
			avail += (a[i]-'0');
		}
		printf("Case #%d: %d\n", tt++, miss);
	}
	return 0;
}

