//darkstallion's template

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<list>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>
#define PI 3.1415926535897932384626433832795
#define eps 1e-9
using namespace std;

int n,ans,arr[150];

void dfs(int i, int z, int val)
{
	if (i == n)
	{
		if (ans == -1)
			ans = val;
		else
			ans = min(ans,val);
	}
	else
	{
		if (arr[i] < z)
			dfs(i+1,z+arr[i],val);
		else
		{
			if (arr[i] < z+z-1)
				dfs(i+1,z+z-1+arr[i],val+1);
			else
			{
				if (z > 1)
					dfs(i,z+z-1,val+1);
				dfs(i+1,z,val+1);
			}
		}
	}
}

int main()
{
	int t;
	scanf("%d",&t);
	FORN(i,t)
	{
		int a;
		scanf("%d%d",&a,&n);
		FORN(j,n)
			scanf("%d",&arr[j]);
		sort(arr,arr+n);
		ans = -1;
		dfs(0,a,0);
		printf("Case #%d: %d\n",i+1,ans);
	}
}
