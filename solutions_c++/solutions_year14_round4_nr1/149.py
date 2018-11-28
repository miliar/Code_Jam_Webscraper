#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
#define MAXN 11000

int N,X,T;
int A[MAXN];
bool S[MAXN];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int i,j,k;
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++)
	{
		scanf("%d%d",&N,&X);
		for (i=0;i<N;i++)
		{
			scanf("%d",&A[i]);
		}
		sort(A,A+N);
		i = 0;
		for (j=N-1;j>0;j--)
		{
			if (A[0] + A[j] <= X)
			{
				break;
			}
		}
		k = j+1;
		int ans = 0;
		while (i < j)
		{
			ans ++;
			if (A[i] + A[j] <= X)
			{
				i++;
				j--;
			}
			else
			{
				j --;
			}
		}
		if (i == j)
		{
			ans ++;
		}
		ans += N - k;
		printf("Case #%d: %d\n",cases,ans);
	}
    return 0;
}
