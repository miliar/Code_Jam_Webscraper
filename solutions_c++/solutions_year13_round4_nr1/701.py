#include <cstdio>
#include <iostream>
#include <map>
using namespace std;

const long long MO = 1000002013;

map<long long,long long> count1, count2;

long long N, M;

long long calcu(long long t)
{
	return (long long)(2*N-t+1)*t/2%MO;
}

int main()
{
	long long T;
	scanf("%lld", &T);
	for(long long tt= 1;tt<=T;tt++)
	{
		scanf("%lld%lld", &N, &M);
		count1.clear();
		count2.clear();
		long long c1 = 0;
		for(long long i = 0;i < M;i++)
		{
			long long u, v, w;
			scanf("%lld%lld%lld", &u, &v, &w);
			if (u==v)
				continue;
			count1[-u] += w;
			count2[v] += w;
			c1 += calcu(v-u) * w;
			c1 = c1 % MO;
		}
		//cout << c1 << endl;
		long long c2 = 0;
		for(map<long long,long long>::iterator it = count1.begin(); it != count1.end(); it++)
		{
			long long u = -it->first, w = it->second;
			while(w > 0)
			{
				map<long long,long long>::iterator it2 = count2.lower_bound(u);
				//cerr << "first " << it2->first << " second" << it2->second << endl;
				if (it2->second > w)
				{
					c2 += calcu(it2->first-u) * w;
					it2->second -= w;
					w = 0;
				}
				else
				{
					c2 += calcu(it2->first-u) * it2->second;
					w -= it2->second;
					it2->second = 0;
				}
				c2 = c2%MO;
				if (it2->second == 0)
					count2.erase(it2);
			}
		}
		//cout << c2 << endl;
		printf("Case #%lld: %lld\n", tt, ((c1-c2)%MO + MO)%MO);
	}
	return 0;
}
