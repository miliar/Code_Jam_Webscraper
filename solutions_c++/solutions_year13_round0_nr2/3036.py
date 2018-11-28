#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

void solve()
{
	int m,n,i,j,k,s,flag=1,f1,f2;
	int l[101][101];

	scanf("%d%d",&m,&n);

	for( i = 0 ; i < m ;i++)
		for (j = 0 ; j < n ; j++)
			scanf("%d",&l[i][j]);

	for (i = 0 ; i < m ; i++)
		for (j = 0 ;j < n; j++)
		{
			f1 = 1;f2 = 1;
			for( k = 1 ; k < m ; k++)
				if(l[(i+k)%m][j] > l[i][j]) f1 = 0;
			for (s = 1 ; s < n ; s++)
				if (l[i][(j+s)%n] > l[i][j]) f2 = 0;
			if (f1==0 && f2 == 0) flag = 0;
		}

	if (flag == 0) printf("NO\n");
	else printf("YES\n");
}

int main()
{
	int T;
	
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
	scanf("%d",&T);
	for (int t = 1 ; t <= T ;t++)
	{
		printf("Case #%d: ",t);
		solve();
	}
return 0;
}