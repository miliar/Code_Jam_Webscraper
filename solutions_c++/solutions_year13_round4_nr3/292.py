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
#include <string.h>
using namespace std;
vector<int> E[2010];
int f[2010],A[2010],B[2010],Num[2010];
bool mark[2010];
vector<int> rec[2010];
int N;
bool check(){
	int i,j;
	for (i=N-1;i>=0;i--){
		f[i] = 1;
		for (j=i+1;j<N;j++)
			if (Num[j]<Num[i])
				f[i] = max(f[i],f[j]+1);
		if (f[i]!=B[i]) return 0;
	}
	return 1;

}
bool dfs(int now){
	if (now==N){
		if (check()) return 1;
		else return 0;
	}
	int i,low, high;
	if (Num[now]!=-1) return dfs(now+1);
	else {
		high = N;
		for (i=0;i<rec[A[now]].size();i++)
			if (rec[A[now]][i]<now)
			high = min(high,Num[rec[A[now]][i]]-1);
			else break;
		low = N;
		if (A[now]==1) low = 1;
		else
		for (i=0;i<rec[A[now]-1].size()&&rec[A[now]-1][i]<now;i++)
			low = min(low,Num[rec[A[now]-1][i]]+1);
		//printf("%d :%d %d\n",now, low, high);
		for (i = low;i<=high;i++)if (!mark[i])
		{
			Num[now] = i;
			mark[i] = 1;
			if (dfs(now+1)) return 1;
			Num[now] = -1;
			mark[i] = 0;
		}


	}
	return 0;
}
int main(){
	int tt,tcas = 1;
	int i;
	scanf("%d",&tt);
	while(tt--){
		scanf("%d",&N);
		for (i=0;i<N;i++)
			scanf("%d",&A[i]);
		for (i=0;i<N;i++)
			scanf("%d",&B[i]);
		for (i=0;i<N;i++) rec[i].clear();
		for (i=0;i<N;i++) rec[A[i]].push_back(i);
		memset(Num,-1,sizeof(Num));
		memset(mark,0,sizeof(mark));

		int t = rec[1].size();
		for (i=0;i<t;i++)
			Num[rec[1][i]] = t-i, mark[t-i] = 1;

		printf("Case #%d:",tcas++);
		if (dfs(0)) {

			for (i=0;i<N;i++)
				printf(" %d",Num[i]);

		}else {
			memset(Num,-1,sizeof(Num));
			memset(mark,0,sizeof(mark));
			Num[rec[1][t-1]] = 1,mark[1] = 1;
			if (dfs(0)) {
						for (i=0;i<N;i++)
							printf(" %d",Num[i]);
			}
		}

		printf("\n");
	}
}




