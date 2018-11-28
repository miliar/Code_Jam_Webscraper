#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

int hash[20];
int Bmap1[5][5];
int Bmap2[5][5];
int K1,K2;
void solve()
{
	vector<int> G;
	G.clear();
	for(int i=1;i<=4;i++)
	{
		hash[Bmap1[K1][i]]=1;
	}
	for(int i=1;i<=4;i++)
	{
		if(hash[Bmap2[K2][i]]==1)
			G.push_back(Bmap2[K2][i]);
	}
	if(G.size()==0)
	{
		printf("Volunteer cheated!\n");
	}else if(G.size()==1)
	{
		printf("%d\n",G[0]);
	}else if(G.size()>1)
	{
		printf("Bad magician!\n");
	}
}


int main()
{
	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int idx=1;idx<=T;idx++)
	{
		memset(hash,0,sizeof(hash));
		scanf("%d",&K1);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
			scanf("%d",&Bmap1[i][j]);
		scanf("%d",&K2);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
			scanf("%d",&Bmap2[i][j]);
		printf("Case #%d: ",idx);
		solve();
	}
	return 0;
}
