#include <stdio.h>
#include <queue>
#include <map>
#include <string>
#include <vector>
#include <memory.h>
#include <algorithm>
using namespace std;
bool Visit[1<<20];
map<string,int> KeyMap;
vector<int> Keys[20];
int Opener[20];
int By[1<<20];

int getKey(const string& key)
{
	if (KeyMap.find(key)==KeyMap.end())
		return KeyMap[key] = KeyMap.size();
	return KeyMap[key];
}
int readKey()
{
	char t[256];
	scanf("%s",&t);
	return getKey(t);
}
int main()
{
	int T;scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		KeyMap.clear();
		memset(Visit,0,sizeof(Visit));
		int M,N;
		scanf("%d %d",&M,&N);
		vector<int> initKeys;
		for (int q=0;q<M;++q) 
			initKeys.push_back( readKey() );
		for (int q=0;q<N;++q)
		{
			Opener[q] = readKey();
			Keys[q].clear();
			int t; scanf("%d",&t);
			for (int w=0;w<t;++w)
				Keys[q].push_back( readKey() );
		}
		Visit[0]=1;
		queue<int> Q;
		Q.push(0);
		while (!Q.empty())
		{
			int state = Q.front(); Q.pop();
			map<int,int> keyCount;
			for (int q=0;q<M;++q)
				keyCount[ initKeys[q] ]++;
			for (int q=0;q<N;++q)
			{
				if (state&(1<<q)) //opened
				{
					keyCount[ Opener[q] ]--;
					for (int w=0;w<Keys[q].size();++w)
						keyCount[ Keys[q][w] ]++;
				}
			}
			for (int q=0;q<N;++q)
			{
				if (state&(1<<q)) continue;
				int next = state | (1<<q);
				if (Visit[next]==false && keyCount[ Opener[q] ]>0)
				{
					Visit[next]=true;
					By[next]=q;
					Q.push(next);
				}
			}
		}
		if (Visit[(1<<N)-1]==false) printf("Case #%d: IMPOSSIBLE\n",kase);
		else
		{
			vector<int> path;
			for (int s=(1<<N)-1;s;s^=(1<<By[s])) path.push_back(By[s]);
			reverse(path.begin(),path.end());
			printf("Case #%d:",kase);
			for (int q=0;q<path.size();++q) printf(" %d",path[q]+1);
			printf("\n");
		}
	}
	return 0;
}
