#include <cstdio>
#include <cstring>
using namespace std;
typedef long long LL;
int main()
{
	int T,n,step,count;
	LL ans,tmp;
	bool used[10];
	scanf("%d",&T);
	for (int cas = 1; cas <= T; ++cas)
	{
		scanf("%d",&n);
		printf("Case #%d: ",cas);
		memset(used,10,sizeof(used));
		count = 0;
		if (n == 0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		for (step = 1; ;++step)
		{
			LL tmp = n;
			tmp *= step;
			ans = tmp;
			while (tmp)
			{
				if (!used[tmp%10])
				{
					used[tmp%10] = true;
					++count;
				}
				tmp /= 10;
			}
			if (count == 10)
				break;
		}
		printf("%d\n", ans);
	}
	return 0;
}