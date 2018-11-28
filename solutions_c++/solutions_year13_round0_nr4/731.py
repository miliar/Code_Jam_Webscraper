#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<functional>
#include<algorithm>

using namespace std;

//#define _INFILE		"D.in"
//#define _OUTFILE	"D.out"

#define _INFILE		"D-small-attempt1.in"
#define _OUTFILE	"D-small.out"

//#define _INFILE		"D-large.in"
//#define _OUTFILE	"D-large.out"

int n, k;
int keyType[200];
vector<int> keys[200];
int kn;
int history[200];
int curKeys[200];
int visited;
char memo[1<<25];

bool go(int d)
{
	if (d == n)
		return true;
	if (memo[visited])
		return false;

	memo[visited] = 1;

	for(int i=0; i<n; i++)
	{
		if ((visited & (1 << i)) || curKeys[keyType[i]] == 0) 
			continue;
		visited |= (1<<i);
		history[d] = i;
		curKeys[keyType[i]]--;

		for(int j=0; j<keys[i].size(); j++)
			curKeys[keys[i][j]]++;

		if (go(d+1))
			return true;


		for(int j=0; j<keys[i].size(); j++)
			curKeys[keys[i][j]]--;
		
		curKeys[keyType[i]]++;
		visited &= ~(1<<i);
	}

	return false;
}

void solve()
{
	scanf("%d%d",&k,&n);
	int checkKeys[200];
	memset(memo, 0, sizeof(memo));
	visited = 0;
	for(int i=0; i<200; i++) {
		keys[i].clear();
		curKeys[i] = 0;
		checkKeys[i] = 0;
	}
	map<int, int> typeMap;
	kn = 0;
	for(int i=0; i<k; i++)
	{
		int kk;
		scanf("%d",&kk);
		if (typeMap.find(kk) == typeMap.end())
			typeMap[kk] = kn++;
		curKeys[typeMap[kk]]++;
		checkKeys[typeMap[kk]]++;
	}
	for(int i=0; i<n; i++)
	{
		int kk, tt;
		scanf("%d%d",&tt, &kk);
		if (typeMap.find(tt) == typeMap.end())
			typeMap[tt] = kn++;
		
		keyType[i] = typeMap[tt];
		for(int j=0; j<kk; j++)
		{
			int tt;
			scanf("%d",&tt);
			if (typeMap.find(tt) == typeMap.end())
				typeMap[tt] = kn++;
			keys[i].push_back(typeMap[tt]);
			checkKeys[typeMap[tt]]++;
		}
	}

	for(int i=0; i<n; i++)
	{
		if (checkKeys[keyType[i]] == 0)
		{
			printf(" IMPOSSIBLE\n");
			return;
		}
	}
	if (go(0))
	{
		for(int i=0; i<n; i++)
			printf(" %d", history[i] + 1);
		printf("\n");
		return;
	}

	printf(" IMPOSSIBLE\n");
}

int main(void)
{
	int T;
	freopen(_INFILE, "r", stdin);
	freopen(_OUTFILE, "w", stdout);

	scanf("%d",&T);

	for(int i=0; i<T; i++)
	{
		printf("Case #%d:", i+1);
		solve();
	}
	return 0;
}

