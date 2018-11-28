#include <stdio.h>
#include <string.h>
#include <vector>
#include <queue>
#include <cassert>
#include <map>
#include <set>
#include <stack>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ", ++TK);

		int P = 0;
		scanf("%d",&P);
		map<int, int> oops;
		static int what[11111];
		static int freq[11111];
		for(int i = 0;i < P;i++) scanf("%d",&what[i]);
		for(int i = 0;i < P;i++) scanf("%d",&freq[i]);
		for(int i = 0;i < P;i++) oops[what[i]] = freq[i];
		
		vector<int> result;
		oops[0]--;
		for(auto it = oops.begin();it != oops.end();++it)
		{
			while(it->second)
			{
				result.push_back(it->first);
				
				for(int i = 0;i < (1<<(result.size()-1));i++)
				{
					int sum = it->first;
					for(int j = 0;j < result.size()-1;j++)
					{
						if(i & (1<<j)) sum += result[j];
					}
					assert(oops[sum] > 0);
					oops[sum]--;
				}
			}
		}

		for(auto x: result) printf("%d ",x);
		puts("");
	}
	return 0;
}
