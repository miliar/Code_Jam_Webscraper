#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>
using namespace std;
#pragma comment(linker, "/STACK:50000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "B-large";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
}


int dp[1010][1010];
int oo = 1<<29;
int go(int n, int k)
{
	if (n==0) return 0;
	if (k==0) return oo;
	if (dp[n][k]!=-1) return dp[n][k];

	int res = go(n-1,k-1);
	res = min(res,go(n,k-1));

	for (int i=1;i<n;i++)
		res = min(res, 1 + go(i,k) + go(n-i,k) );
	
	return dp[n][k] = res;
}


int main() {

	init();


	
	int tst;
	scanf("%d\n",&tst);

	memset(dp,-1,sizeof(dp));

	for (int cas = 1; cas<=tst;cas++)
	{
		int d;
		vi a;
		scanf("%d",&d);
		int res = 0;
		for (int i=0;i<d;i++)
		{
			int t;
			scanf("%d",&t);
			a.push_back(t);
			res = max(res,t);
		}

		int mx = res;
		for (int i=1;i<=mx;i++)
		{
			int cur = 0;
			for (int j=0;j<sz(a);j++)
				cur+=go(a[j],i);
			res = min(res,cur+i);
		
		}

		printf("Case #%d: %d\n",cas,res);
	}
	
	
	
	

	return 0;
}

