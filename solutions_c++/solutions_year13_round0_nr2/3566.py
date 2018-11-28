/*
 * Q-Lawnmower.cpp
 *
 *  Created on: Apr 13, 2013
 *  Author: mohamedgamal
 *  Tags:
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <queue>
using namespace std;
#define mp(X,Y) make_pair((X),(Y))
#define SZ(X) (int)((X).size())
typedef pair<int,int> pii;
int const MAX = 102;
int const OO = (1<<28);
int grid[MAX][MAX];
int N,M;
set <int> S;
int temp[MAX][MAX];
bool valid(int r,int c,int v)
{
	bool v1 = false,v2=false;
	for(int j=0;j<M;++j)
		v1|=(temp[r][j]>v && temp[r][j]==grid[r][j]);
	for(int i=0;i<N;++i)
		v2|=(temp[i][c]>v && temp[i][c]==grid[i][c]);
	return !v1 || !v2;
}
bool can(vector<int> V)
{

	for(int k=0;k<SZ(V);++k)
	{
		for(int i=0;i<N;++i)
		{
			for(int j=0;j<M;++j)
			{
				if(grid[i][j]== V[k])
				{
					if(!valid(i,j,V[k]))
						return false;
					temp[i][j]=V[k];
				}
			}
		}
	}
	return true;
}
int main()
{
	freopen("in.in","rt",stdin);
	freopen("out.out","wt",stdout);
	int t,id=1;
	scanf("%d",&t);
	while(t--)
	{
		S.clear();
		memset(temp,0,sizeof(temp));
		scanf("%d%d",&N,&M);
		for(int i=0;i<N;++i)
			for(int j=0;j<M;++j)
			{
				scanf("%d",&grid[i][j]);
				S.insert(grid[i][j]);
			}
		printf("Case #%d: ",id++);
		if(can(vector<int>(S.rbegin(),S.rend())))
		{
			printf("YES\n");
		}
		else
			printf("NO\n");
	}
}
