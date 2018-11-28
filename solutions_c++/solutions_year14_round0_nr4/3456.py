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
#define NUM 1000000
using namespace std;

int n,dp[1010][1010];
vector<int>a,b;

int solve(int idx1,int idx2)
{
	int i,j,k,ans=0;
	if(idx1==n||idx2==n)
		return dp[idx1][idx2]=0;
	
	if(dp[idx1][idx2]==-1)
	{
		if(a[idx1]>b[idx2])
			ans=1+solve(idx1+1,idx2+1);
		else
			ans = solve(idx1+1,idx2);
	  
		dp[idx1][idx2]=ans;		
	}
	
	return dp[idx1][idx2];
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,t,cnt,ans1,ans2,cases;
	double d;
	scanf("%d",&t);
	for(cases=1;cases<=t;cases++)
	{
		scanf("%d",&n);
		a.clear();
		b.clear();
		for(i=1;i<=n;i++)
		{
			scanf("%lf",&d);
			//printf("%lf %lf\n",d,d*1000000);
			j = d*NUM;
			a.push_back(j);
			
		}
		for(i=1;i<=n;i++)
		{
			scanf("%lf",&d);
			j = d*NUM;
			b.push_back(j);
			
		}
		
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		for(i=0;i<=n+1;i++)
			for(j=0;j<=n+1;j++)
			dp[i][j]=-1;
		cnt = 0;
		k=0;
		for(i=0;i<n;i++)
		{
			for(j=k;j<n;j++)
			{
				// printf("i=%d j=%d\n",a[i],b[j]);
				if(a[i]<b[j])
				{
					cnt++;
					k=j+1;
					break;
				}
			}
			
		}
	//	printf("cnt=%d\n",cnt);
		ans2 = n-cnt;
		ans1 = solve(0,0);
		printf("Case #%d: %d %d\n",cases,ans1,ans2);
		
	}
	
	return 0;
}