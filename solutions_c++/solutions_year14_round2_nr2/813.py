#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int a,b,k;
		scanf("%d %d %d",&a,&b,&k);
		int ret=0;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if((i&j)<k)
				{
					ret++;
				}
			}
		}
		printf("Case #%d: %d\n",t,ret);
	}
	return 0;
}
