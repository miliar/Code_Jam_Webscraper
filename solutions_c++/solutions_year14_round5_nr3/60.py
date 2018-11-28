#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int etype[1111];
int eid[1111];
int state[1111];

int ids[23];
int idcnt = 0;
int N = 0;
int ans = 0;
int inside = 0;
int ooxxcnt = 0;

int dfs(int x)
{
	if(x == N)
	{
		ans = min(ans,inside);
		return 0;
	}
	if(eid[x] != 0)
	{
		if(etype[x] == 0)
		{
			int back = state[eid[x]];
			if(state[eid[x]] == 1) return 0;
			state[eid[x]] = 1;
			inside++;
			dfs(x+1);
			inside--;
			state[eid[x]] = back;
		}
		else
		{
			int back = state[eid[x]];
			if(!back) inside++;
			if(state[eid[x]] == 2) return 0;
			state[eid[x]] = 2;
			inside--;
			dfs(x+1);
			inside++;
			state[eid[x]] = back;
			if(!back) inside--;
		}
	}
	else
	{
		if(etype[x] == 0)
		{
			for(int i = 0;i < idcnt;i++)
			{
				int back = state[ids[i]];
				if(state[ids[i]] == 1) continue;
				state[ids[i]] = 1;
				inside++;
				dfs(x+1);
				inside--;
				state[ids[i]] = back;
			}
			ooxxcnt++;
			inside++;
			dfs(x+1);
			inside--;
			ooxxcnt--;
		}
		else
		{
			for(int i = 0;i < idcnt;i++)
			{
				int back = state[ids[i]];
				if(!state[ids[i]]) inside++;
				if(state[ids[i]] == 2) continue;
				state[ids[i]] = 2;
				inside--;
				dfs(x+1);
				inside++;
				state[ids[i]] = back;
				if(!state[ids[i]]) inside--;
			}
			if(ooxxcnt)
			{
				ooxxcnt--;
				inside--;
				dfs(x+1);
				inside++;
				ooxxcnt++;
			}
			else dfs(x+1);
		}
	}
	return 0;
}

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d",&T);
	while(T--)
	{
		idcnt = 0;
		printf("Case #%d: ",++TK);
		scanf("%d",&N);
		for(int i = 0;i < N;i++)
		{
			char ev[4] = {0};
			int id = 0;
			scanf("%s %d",ev,&id);
			if(ev[0] == 'E') etype[i] = 0;
			else etype[i] = 1;
			eid[i] = id;
			if(id) ids[idcnt++] = id;
		}
		sort(ids,ids+idcnt);
		idcnt = unique(ids,ids+idcnt)-ids;

		ans = ~0U>>1;
		inside = 0;
		ooxxcnt = 0;
		memset(state,0,sizeof(state));
		dfs(0);
		if(ans == ~0U>>1) puts("CRIME TIME");
		else printf("%d\n",ans);
	}
	while(getchar() != EOF);
	return 0;
}
