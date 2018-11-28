#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

int main()
{
	freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);

	int T, N, pick, tmpN, div, cnt, cas;
	bool used[10];
	scanf("%d", &T);
	for (cas = 1; cas <= T; ++cas)
	{
		scanf("%d", &N);
		printf("Case #%d: ", cas);
		
		if (N == 0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		
		memset(used, false, sizeof(used));
		cnt = 0;
		pick = 0;
		while (cnt < 10)
		{
			pick += N;
			tmpN = pick;
			while (tmpN)
			{
				div = tmpN%10;
				if (used[div] == false)
				{
					used[div] = true;
					++cnt;
				}
				tmpN /= 10;
			}
		}
		
		printf("%d\n", pick);
	}

	return 0;
}