#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int num[1111];
int sorted[1111];
bool used[1111];

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++TK);
		int N = 0;
		scanf("%d",&N);
		for(int i = 0;i < N;i++) scanf("%d",&num[i]);
		map<int,int> mapping;
		for(int i = 0;i < N;i++) mapping[num[i]] = i;
		for(int i = 0;i < N;i++) sorted[i] = num[i];
		memset(used,0,sizeof(used));
		sort(sorted,sorted+N);
		int ans = 0;
		for(int i = 0;i < N;i++)
		{
			int pos = mapping[sorted[i]];
			int lneed = 0;
			int rneed = 0;
			for(int j = 0;j < pos;j++) if(!used[j]) lneed++;
			for(int j = pos+1;j < N;j++) if(!used[j]) rneed++;
			used[pos] = true;
			ans += min(lneed,rneed);
		}
		printf("%d\n",ans);
	}
	return 0;
}