#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

bool p[10];

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	
	int t,t1;
	scanf("%d",&t);
	while (t--)
	{
		int n;
		t1++;
		scanf("%d",&n);
		if (!n)
		{
			printf("Case #%d: INSOMNIA\n",t1);
			continue;
		}
		memset(p,0,sizeof(p));
		int tot = 0,m = n;
		n = 0;
		while (tot<10)
		{
			n = n + m;
			int nn = n;
			while (nn)
			{
				int tt = nn % 10;
				if (!p[tt])
				{
					p[tt] = 1;
					tot ++;
				}
				nn = nn / 10;
			}
		}
		printf("Case #%d: %d\n",t1,n);
	}
	
	return 0;
}