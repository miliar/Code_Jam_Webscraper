#include<cstdio>
using namespace std;
#define MAXN 111

int T;
int N,M;
int A[MAXN][MAXN];

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int i,j,k;
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++)
	{
		scanf("%d%d",&N,&M);
		for (i=0;i<N;i++)
			for (j=0;j<M;j++)
			{
				scanf("%d",&A[i][j]);
			}
			
		for (i=0;i<N;i++)
			for (j=0;j<M;j++)
			{
				bool b1 = 1,b2 = 1;
				for (k=0;k<N;k++)
					if (A[k][j] > A[i][j])
						b1 = 0;
				for (k=0;k<M;k++)
					if (A[i][k] > A[i][j])
						b2 = 0;
				if (!b1 && !b2)
					goto HERE;
			}
	HERE:
		printf("Case #%d: ",cases);
		if (i < N)
			printf("NO\n");
		else
			printf("YES\n");
	}
	return 0;
}
