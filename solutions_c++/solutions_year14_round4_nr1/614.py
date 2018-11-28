#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

const int MAXN = 20001;
const int MAXM = 2000011;
const int MAXK = 201;
const int INF = 1000000001;
const double eps = 1e-5;

int a[MAXN];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int m,n;
	int T,cas,i,ans,res,j;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		sort(a,a+n);
		ans=0;
		for(i=n-1,j=0;i>=j;i--)
		{
			ans++;
			res=m-a[i];
			if(j<i&&a[j]<=res)
				j++;
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}