#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <algorithm>
#define MAXN 10005

using namespace std;

int main ()
{
	int T, iT;
	scanf("%d",&T);
	static int a[MAXN];
	static char b[MAXN];
	for (iT = 0; iT < T; iT++)
	{
		int N, K;
		scanf("%d %d",&N,&K);
		int i;
		for (i = 0; i < N; i++) scanf("%d",&(a[i]));
		sort(a,a+N);
		memset(b,0,sizeof(b));
		int res = 0;
		int j;
		for (i = N-1; i >= 0; i--)
		{
			if (!b[i])
			{
				b[i] = 1;
				j = N-1;
				while ((j >= 0) && ((b[j]) || ((a[i] + a[j]) > K))) j--;
				if (j >= 0) b[j] = 1;
				res++;
			}
		}
		printf("Case #%d: %d\n",iT+1,res);
	}
	return 0;
}
