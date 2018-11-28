#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("a_out.txt","w",stdout);
	int T;
	int cas = 0;
	scanf("%d",&T);
	while(T--)
	{
		uint64_t N,val;
		bool flag[10];
		memset(flag,false,sizeof(flag));
		scanf("%llu",&N);
		unordered_set<uint64_t> dict;
		int i = 1;
		bool cando = false;
		for(;;++i)
		{
			val = N * i;
			if(dict.find(val) != dict.end())
				break;
			dict.insert(val);
			while(val)
			{
				flag[val % 10] = true;
				val /= 10;
			}
			bool flg = true;
			for(int j = 0; j < 10; ++j)
				if(!flag[j])
				{
					flg = false;;
					break;
				}
			if(flg)
			{
				cando = true;
				break;
			}
		}
		printf("Case #%d: ",++cas);
		if(cando)
			printf("%llu\n",(uint64_t)i * N);
		else
			printf("INSOMNIA\n");

	}
	return 0;
}
