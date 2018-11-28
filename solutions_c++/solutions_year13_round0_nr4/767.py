#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<cstdio>
#include<cassert>
#include<iostream>
#include<queue>
#include<map>
#include<set>
#include<vector>
#include<ctime>

using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b)  ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))

#define MP make_pair
#define pb push_back
#define inf  1000000000
#define maxn 100001
#define maxc 100001
#define MP make_pair

//typedef long long LL;
typedef pair<int,int> pi;
typedef pair<pi,pi> pii;
typedef __int64 LL;

vector<int> box[25],res;
int cnt[202];
int need[25],n;
int memo[1<<20];


int solve(int mask)
{
	int ret=0,i,j;

	if(mask+1==(1<<n)) return 1;
	if(memo[mask]!=-1) return memo[mask];


	for(i=0;i<n;i++)
	{
		 if(mask&(1<<i)) continue;
		 if(cnt[need[i]]==0) continue;

		 --cnt[need[i]];
		 for(j=0;j<box[i].size();j++) cnt[box[i][j]]++;

		 int q=solve(mask|(1<<i));

		 if(q)
		 {
			 ret=1;
			 res.pb(i+1);
			 break;
		 }

		 ++cnt[need[i]];
		 for(j=0;j<box[i].size();j++) cnt[box[i][j]]--;
	}

	return memo[mask]=ret;
}

int main()
{
	int i,j,k,tests,cs=0,K;
	string s;
	

	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	scanf("%d",&tests);

	while(tests--)
	{	
		scanf("%d%d",&K,&n);
		MEM(cnt,0);
		int x;
		for(i=0;i<K;i++)
		{
			cin>>x;
			--x;
			cnt[x]++;
		}

		MEM(memo,-1);
		res.clear();

		for(i=0;i<n;i++)
		{
			scanf("%d",&need[i]);
			--need[i];
			cin>>k;
			box[i].clear();
			while(k--)
			{
				cin>>x;
				--x;
				box[i].pb(x);
			}
		}
	
		printf("Case #%d:",++cs);
		int q=solve(0);

		if(q==0)
			puts(" IMPOSSIBLE");
		else
		{
			for(i=n-1;i>=0;i--)
				printf(" %d",res[i]);
			puts("");
		}
	}

	return 0;
} 
