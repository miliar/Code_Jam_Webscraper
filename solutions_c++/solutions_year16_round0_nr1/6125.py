#include <cstdio>
#include <iostream>
#include <cstring>
#include <set>
using namespace std;
bool flag[10];
set<long long> used;

int main()
{
	long long a;
	int cas;
	scanf("%d", &cas);
	for(int z=1; z<=cas; z++)
	{
		scanf("%lld", &a);
		memset(flag, false, sizeof flag);
		used.clear();
		int cnt = 0;
		int mul = 0;
		bool fail = false;
		while(cnt!=10)
		{
			mul++;
			long long tmp = a*mul;
			if(used.find(tmp)!=used.end())
			{
				fail = true;
				break;
			}
			used.insert(tmp);
			int digit;
			while(tmp>0)
			{
				digit = tmp%10;
				tmp /= 10;
				if(!flag[digit])
					flag[digit]=true, cnt++;
			}
		}
		printf("Case #%d: ", z);
		if(fail)
			puts("INSOMNIA");
		else
			printf("%lld\n", a*mul);
	}
	return 0;
}
