#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cstring>
#define SIZE 205
#define MAX_S 1000000000

using namespace std;

vector <int> vec;
vector <int> key[SIZE];
bool check[MAX_S];
int kind[SIZE];
int num[SIZE];
int n,k;

bool dfs(int S=0)
{
	if(S==(1<<k)-1)
	{
		for(int i=0;i<vec.size();i++)
		{
			if(i!=0) printf(" ");
			printf("%d",vec[i]);
		}printf("\n");
		return true;
	}
	for(int i=0;i<k;i++)
	{
		if((!(S>>i&1))&&(!check[S|1<<i])&&num[kind[i]]>=1)
		{
			S|=1<<i;
			check[S]=true;
			num[kind[i]]--;
			for(int j=0;j<key[i].size();j++) num[key[i][j]]++;
			vec.push_back(i+1);
			if(dfs(S)) return true;
			vec.pop_back();
			for(int j=0;j<key[i].size();j++) num[key[i][j]]--;
			num[kind[i]]++;
			S-=1<<i;
		}
	}
	return false;
}
void init()
{
	memset(num,0,sizeof(num));
	memset(check,false,sizeof(check));
	memset(kind,0,sizeof(kind));
	vec.clear();
	for(int i=0;i<SIZE;i++) key[i].clear();
}
void solve()
{
	init();
	scanf("%d %d",&n,&k);
	for(int i=0;i<n;i++)
	{
		int x;
		scanf("%d",&x);x--;
		num[x]++;
	}
	for(int i=0;i<k;i++)
	{
		scanf("%d",&kind[i]);kind[i]--;
		int a;
		scanf("%d",&a);
		for(int j=0;j<a;j++)
		{
			int x;
			scanf("%d",&x);x--;
			key[i].push_back(x);
		}
	}
	if(!dfs()) printf("IMPOSSIBLE\n");
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		printf("Case #%d: ",i+1);
		solve();
	}
}
