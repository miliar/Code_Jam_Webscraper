#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
	int tc, t, i, x, y, a, b, k;
	long pair;

	freopen("inp_lottery.txt","r",stdin);
	freopen("out_lottery.txt","w",stdout);

	scanf("%d",&tc);

	for(i=1; i<=tc; i++)
	{
		scanf("%d %d %d",&a,&b,&k);

		pair=0;
		for(x=0; x<a; x++)
		{
			for(y=0; y<b; y++)
			{
				if((x & y)<k)
					pair++;
			}
		}

		printf("Case #%d: %ld\n",i,pair);
	}

	return 0;
}