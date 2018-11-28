#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = (1 << 12) + 5;
const char Ref[3] = {'R','P','S'};

int N,cnt[3],Bot[MAXN],Ans[MAXN],cur;

void Dfs(int top,int l,int r)
{
	if (l == r) Bot[l] = top,cnt[top] --; else
	{
		int mid = l + r >> 1;
		Dfs(top,l,mid);
		Dfs((top + 2) % 3,mid + 1,r);
		bool small = 0;
		for(int i = 0;i <= mid - l;i ++)
			if (Ref[Bot[l + i]] < Ref[Bot[mid + 1 + i]]) {small = 1;break;} else
				if (Ref[Bot[l + i]] > Ref[Bot[mid + 1 + i]]) {small = 0;break;}
		if (!small)
		{
			for(int i = 0;i <= mid - l;i ++)
				swap(Bot[l + i],Bot[mid + 1 + i]);
		}
	}
}

void Work(int Case)
{
	printf("Case #%d: ", Case);
	scanf("%d%d%d%d", &N, &cnt[0], &cnt[1], &cnt[2]);
	bool get = 0;
	for(int i = 0;i < 3;i ++)
	{
		int bak[3];
		memcpy(bak,cnt,sizeof bak);
		cur = 0;
		Dfs(i,0,(1 << N) - 1);
		bool ok = 1;
		for(int j = 0;j < 3;j ++)
			if (cnt[j] < 0) {ok = 0;break;}
		memcpy(cnt,bak,sizeof cnt);
		if (!ok) continue;
		if (!get) 
		{
			for(int j = 0;j < (1 << N);j ++) Ans[j] = Bot[j];
			get = 1;
			continue;
		} 
		bool small = 0;
		for(int j = 0;j < (1 << N);j ++)
			if (Ref[Bot[j]] < Ref[Ans[j]]) {small = 1;break;} else
				if (Ref[Bot[j]] > Ref[Ans[j]]) {small = 0;break;}
		if (small)
			for(int j = 0;j < (1 << N);j ++) Ans[j] = Bot[j];
	}
	if (!get) printf("IMPOSSIBLE\n"); else
	{
		for(int j = 0;j < (1 << N);j ++)
		{
			printf("%c", Ref[Ans[j]]);
		}
		printf("\n");
	}
}

int main()
{
	freopen("data.in","r",stdin);
	int T;
	scanf("%d", &T);
	for(int i = 1;i <= T;i ++)
		 Work(i);
	return 0;
}
