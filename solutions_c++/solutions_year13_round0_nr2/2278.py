#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#define INF 1000000007
#define EPS 0.000000001
using namespace std;

int T,n,m,i,j;
int a[111][111],b[111],c[111];

int main()
{
//	freopen("2.in","r",stdin);
//	freopen("2.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&a[i][j]);
		for(i=0;i<n;i++)
			b[i] = 0;
		for(j=0;j<m;j++)
			c[j] = 0;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				b[i] = max(b[i],a[i][j]);
		for(j=0;j<m;j++)
			for(i=0;i<n;i++)
				c[j] = max(c[j],a[i][j]);
		bool l=true;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				if(min(b[i],c[j])!=a[i][j])
					l=false;
		if(l)
			printf("YES\n"); else
			printf("NO\n");
	}
	return 0;
}