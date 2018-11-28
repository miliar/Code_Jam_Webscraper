#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <functional>
#include <limits>
#include <cassert>
#include <sstream>
#include <cmath>
#include <string>
#include <fstream>

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

const int max_n=1010;

int n,T;
int a[max_n],B[max_n],A[max_n];
int dp[max_n][max_n];
pair<int,int> P[max_n];

int main()
{
	scanf("%d",&T);

	for(int z=0; z<T; z++)
	{
		scanf("%d",&n);
		for(int i=0; i<n; i++)
		{
			scanf("%d",&a[i]);
			P[i]=pii(a[i],i);
		}

		sort(P,P+n);

		fill(B,B+n,0);
		fill(A,A+n,0);
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<i; j++)
				B[i]+=(a[j]<a[i]);
			for(int j=i+1; j<n; j++)
				A[i]+=(a[j]<a[i]);
		}

		for(int i=0; i<=n; i++)
			for(int j=0; j<=n; j++)
				dp[i][j]=1e9;

		dp[0][0]=0;
		for(int i=0; i<n; i++)
			for(int j=0; i+j<n; j++)
			{
				int k=P[i+j].second;
				dp[i+1][j]=min(dp[i+1][j],dp[i][j]+k-B[k]);
				dp[i][j+1]=min(dp[i][j+1],dp[i][j]+n-(k+1)-A[k]);
			}

		// for(int i=0; i<=n; i++)
		// 	for(int j=0; i+j<=n; j++)
		// 		cout<<i<<" "<<j<<" "<<dp[i][j]<<"\n";

		int res=1e9;
		for(int j=0; j<=n; j++)
			res=min(res,dp[n-j][j]);

		printf("Case #%d: %d\n",z+1,res);
	}

	return 0;
}	