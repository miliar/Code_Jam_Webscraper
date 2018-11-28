#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

int T, A, B, K;

int main()
{	int tt, i, j, cnt, t;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for(tt=0; tt<T; ++tt)
	{
		scanf("%d %d %d", &A, &B, &K);
		cnt=0;
		for(i=0; i<A; ++i)
			for(j=0; j<B; ++j)
			{
				t = i&j;			
				if(t < K)
					cnt++;
			}
		printf("Case #%d: %d\n", tt+1, cnt);
	}

	return 0;
}