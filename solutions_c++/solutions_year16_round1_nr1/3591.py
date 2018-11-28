#include <stdio.h>
#include <string.h>
#include <list>
#include <iostream>
#include <string>
using namespace std;
int main()
{
	int t, i, n, len;
	char sz[1024];
	char ans[1024];
	list<char> x;
	list<char>::iterator it;
	scanf("%d", &t);
	for(i = 1; i <= t; ++i)
	{
		scanf("%s", sz);
		len = strlen(sz);
		x.clear();
		x.push_front(sz[0]);
		for(n = 1; n < len; ++n)
		{
			if(x.front() <= sz[n])
			{
				x.push_front(sz[n]);
			}
			else
			{
				x.push_back(sz[n]);
			}
		}

		n = 0;
		for(it = x.begin(); it != x.end(); ++it)
		{
			ans[n] = *it;
			++n;
		}
		ans[n] = 0;
		
		printf("Case #%d: %s\n", i, ans);		
	}
	return 0;
}
