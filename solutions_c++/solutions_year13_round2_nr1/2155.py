#include <cstdio>
#include <algorithm>
using namespace std;

int sz[110];

int run(int a, int l, int r)
{
	if(l==r) return 0;
	if(a>sz[l]) return run(a+sz[l], l+1, r);
	return min(run(a+a-1, l, r)+1, run(a, l, r-1)+1);
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		int a, n;
		scanf("%d%d", &a, &n);
		for(int i=0; i<n; i++)
			scanf("%d", &sz[i]);
		if(a==1){ printf("Case #%d: %d\n", t, n); continue; }
		sort(sz, sz+n);
		printf("Case #%d: %d\n", t, run(a, 0, n));
	}
	return 0;
}
