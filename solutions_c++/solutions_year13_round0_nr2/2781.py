#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

#define sz 105

int g[sz][sz];
int max_row[sz];
int max_column[sz];

bool soln(int N, int M){
	
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			if (g[i][j] < max_row[i] && g[i][j] < max_column[j])
			{
				return false;
			}
		}
	}
	return true;
}

void init(int N,int M){
	for (int i = 0; i < N; ++i)
	{
		max_row[i] = -1;
	}
	
	for (int j = 0; j < M; ++j)
	{
		max_column[j] = -1;
	}
}

int main(){
	
	int cas = 1,N,M,T;  
	
	freopen("iii.txt", "r", stdin);
	freopen("o.txt", "w", stdout);
	
	scanf("%d",&T);
	while(T--){
		scanf("%d %d",&N,&M);
		init(N,M);
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < M; ++j)
			{
				scanf("%d",&g[i][j]);
				
				if (g[i][j] >  max_column[j])
				{
					max_column[j] = g[i][j];
				}
				if (g[i][j] > max_row[i])
				{
					max_row[i] = g[i][j];
				}
			}
		}
		if (soln(N,M))
		{
			printf("Case #%d: YES\n",cas++);
		}
		else
		{
			printf("Case #%d: NO\n",cas++);
		}
		
	}
	
	
	
	return 0;
}