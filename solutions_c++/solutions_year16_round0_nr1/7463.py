#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <map>
using namespace std;
#define LL long long
map <LL, bool> mp;



int main()
{
	int T,cas = 1;
	scanf("%d",&T);
	LL n;
	while(T--)
	{
		scanf("%lld",&n);
		mp.clear();
		bool isok[10] = {false};
		int okcnt = 0;
		bool has_res = true;
		LL base = n;
		while(true)
		{
			if(mp.find(n) != mp.end())
			{
				has_res = false;
				break;
			}
			mp[n] = true;
			LL tmp = n;
			
			while(tmp)
			{
				int gewei = tmp % 10;
				if(!isok[gewei])
					isok[gewei] = true, okcnt ++;
				tmp /= 10;
			}
			//printf("n = %lld, okcnt = %d\n",n,okcnt);
			if(okcnt == 10)
				break;
			n += base;
		}
		printf("Case #%d: ", cas++);
		if(has_res)
		{
			printf("%lld\n",n);
		}
		else
		{
			printf("INSOMNIA\n");
		}
	}
	return 0;
}