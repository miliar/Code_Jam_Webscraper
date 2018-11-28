#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define MAXM 1011

long long modulo = 1000002013LL;

int T;
int N,M;

struct pas
{
	int a,b,p;
}A[MAXM];
int B[MAXM*10],Bn;
long long C[MAXM*10],Cn;

long long Ans0,Ans1;

long long getFee(long long n)
{
	return (2LL*N - n+1)*n/2;
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int i,j,k;
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++)
	{
		scanf("%d%d",&N,&M);
		Ans0 = Ans1 = 0LL;
		for (i=0;i<M;i++)
		{
			scanf("%d%d%d",&A[i].a,&A[i].b,&A[i].p);
			Ans0 += getFee(A[i].b - A[i].a) % modulo * A[i].p;
			Ans0 %= modulo;
			B[i*2] = A[i].a;
			B[i*2+1] = A[i].b;
		}
		sort(B,B+2*M);
		Bn = unique(B,B+2*M) - B;
		Cn = Bn;
		memset(C,0,sizeof C);
		
		for (i=0;i<M;i++)
		{
			A[i].a = lower_bound(B,B+Bn,A[i].a) - B;
			A[i].b = lower_bound(B,B+Bn,A[i].b) - B;
			for (j=A[i].a;j<A[i].b;j++)
				C[j] += A[i].p;
		}
		
		bool out = 0;
		while (!out)
		{
			out = 1;
			for (i=0;i<Cn;)
			{
				long long p = 1LL << 40;
				for (j=i;C[j];++j)
				{
					p = min(C[j],p);
				}
				k = j;
				Ans1 += getFee(B[j]-B[i]) % modulo * p;
				Ans1 %= modulo;
				for (j=i;j<k;++j)
				{
					C[j] -= p;
				}
				if (k == i)
				{
					i = k+1;
				}
				else
				{
					out = 0;
					i = k;
				}
			}
		}
		printf("Case #%d: %I64d\n",cases,(Ans0 + modulo - Ans1) % modulo);
	}
}
