#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <climits>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>
using namespace std;
typedef long long LL;
const int MOD =1e9 + 7;
const int INF = 0x3f3f3f3f;

int N,M;
int Mp[105][105];
int Get[105][105];
int Col[105];
int Row[105];
int Fun()
{
	if(N==1||M==1) return 1;
	int i,j,k;
	for(i=1;i<=N;++i)
		for(j=1;j<=M;++j)
			Get[i][j]=1;
	for(i=1;i<=N;++i)
		for(j=1;j<=M;++j)
		{
			if(!Mp[i][j])
			{
				if(!Row[i])
				{
					for(k=1;k<=M;++k)
					{
						Get[i][k]=0;
					}
				}
				if(!Col[j])
				{
					for(k=1;k<=N;++k)
					{
						Get[k][j]=0;
					}
				}
			}
		}
	/*
	for(i=1;i<=N;++i)
	{
		for(j=1;j<=M;++j)
			printf("%d ",Get[i][j]);
		puts("");
	}
	*/
	int flag=1;
	for(i=1;i<=N;++i)
		for(j=1;j<=M;++j)
			if(Get[i][j]!=Mp[i][j])
				return 0;
	return 1;
}
int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int kas=1;kas<=T;++kas)
	{
		int i,j,k;
		scanf("%d%d",&N,&M);
		memset(Mp,-1,sizeof(Mp));
		memset(Col,0,sizeof(Col));
		memset(Row,0,sizeof(Row));
		for(i=1;i<=N;++i)
			for(j=1;j<=M;++j)
			{
				scanf("%d",&Mp[i][j]);
				--Mp[i][j];
			}
		for(i=1;i<=N;++i)
			for(j=1;j<=M;++j)
			{
				if(Mp[i][j])
				{
					Col[j]=1;
					Row[i]=1;
				}
			}
		printf("Case #%d: %s\n",kas,Fun()?"YES":"NO");
	}
	
	
	return 0;
}
