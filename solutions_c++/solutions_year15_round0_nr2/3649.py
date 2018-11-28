#include <cstdio>
#include <iostream>
#include <string>
#include <set>

using namespace std;

const int max_n = 1010;
const int inf = 1e9;
int T,n;
int a[max_n];

int main()
{
	scanf("%d",&T);
	for(int z = 0; z < T; z++)
	{
		scanf("%d",&n);
		int M = 0;
		for(int i = 0; i < n; i++)
		{
			scanf("%d",&a[i]);
			M = max(M,a[i]);
		}

		int res = inf;

		for(int m=1; m<=M; m++)
		{
			int cnt = m;
			for (int i=0; i<n; i++)
				cnt += (a[i]-1)/m;
			res = min(res,cnt);
		}

		printf("Case #%d: %d\n",z+1,res);
	}

	return 0;
}