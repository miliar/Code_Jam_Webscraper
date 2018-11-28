#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define mod 1000002013
using namespace std;
#define M 2005
typedef long long LL;
struct node
{
	LL x;
	LL s;
	LL num;
	bool operator<(const node &a)const
	{
		if(a.x == x)
			return num > a.num;
		return x < a.x;
	}
};
node pos[M];
LL get(LL num, LL n)
{
	LL ans = (num * (n + n - num + 1) / 2) % mod;
	return ans;
}
int main()
{
	LL n, m;
	LL i, j;
	LL x, y, num;
	int tcase, icase = 1;
	scanf("%d", &tcase);
	while(tcase--)
	{
		scanf("%lld%lld", &n, &m);
		j = 0;
		for(i = 0; i < m; i++)
		{
			scanf("%lld%lld%lld\n", &x, &y, &num);
			pos[j].x = x;
			pos[j].num = num;
			j++;
			pos[j].x = y;
			pos[j].s = x;
			pos[j].num = -num;
			j++;
		}
		num = j;
		LL sum = 0;
		sort(pos, pos + num);
		/*for(i = 0; i < num; i++)
		{
			printf("%lld %lld\n", pos[i].x, pos[i].num);
		}*/
		for(i = 0; i < num; i++)
		{
			if(pos[i].num < 0)
			{
				for(j = i - 1; j >= 0; j--)
				{
					if(pos[j].num > 0)
					{
						LL t1 = min(pos[j].num, -pos[i].num);
						LL t2 = get(pos[i].x - pos[i].s, n) - get(pos[i].x - pos[j].x, n);
	//					printf("t1 %lld t2 %lld\n", t1, t2);
						t2 %= mod;
						while(t2 < 0)
							t2 += mod;
						sum += ((t1 * t2) % mod);
	//					printf("sum: %lld\n", sum);
						sum %= mod;
						pos[j].num -= t1;
						pos[i].num += t1;
						if(pos[i].num == 0)
							break;
					}	
				}
			}
		}
		printf("Case #%d: %lld\n", icase++, sum);
	}
	return 0;
}
