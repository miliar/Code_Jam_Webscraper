#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
using namespace std;

#define MEM(a, b) memset(a, (b), sizeof(a))
#define CLR(a) memset(a, 0, sizeof(a))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define S(X) ( (X) * (X) )
#define SZ(V) (int )V.size()
#define FORN(i, n) for(i = 0; i < n; i++)
#define FORAB(i, a, b) for(i = a; i <= b; i++)

typedef pair<int,int> PII;
typedef pair<double, double> PDD;

//typedef int LL;
//typedef __int64 LL;

int pos[100], lis[100], u[100];
int A[100], B[100], X[100];
int sat[100];
int N;

int solve(int at)
{
	int i, z, j;

	if(at > N)
	{
		if(B[at-1]!=1) return 0;

		for(i = at - 1; i >= 1; i--)
		{
			z = 1;
			for(j = i + 1; j < at; j++)
				if(X[i] > X[j])
				{
					z = MAX(z, B[j]+1);
				}

			if(z != B[i])
				return 0;
		}

		return 1;

	}

	int left = N - at + 1;
	for(i = at - 1; i >= 1; i--)
	{
		if(sat[i]) continue;

		z = 1;
		for(j = i + 1; j < at; j++)
			if(X[i] > X[j])
			{
				z = MAX(z, B[j]+1);
				if(z > B[i])
					break;
			}

		if(z > B[i])
			return 0;

		if(z == B[i])
			sat[i] = 1;

		if(z + left < B[i])
			return 0;
	}

	for(i = 1; i <= N; i++)
		if(!u[i])
		{
			z = 1;
			X[at] = i;
			for(j = 1; j < at; j++)
				if(X[j] < X[at])
				{
					z = MAX(z, A[j]+1);
					if(z > A[at])
						return 0;
				}

			if(z > A[at])
				return 0;

			if(z != A[at])
				continue;

			sat[i] = 0;
			u[i] = 1;
			if(solve(at+1))
				return 1;

			u[i] = 0;

		}

	return 0;
}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);

	freopen("C-small-attempt1.ans", "w", stdout);
//	freopen("C-large.in", "r", stdin);
//	freopen("C-large.out", "w", stdout);

	int T, ks;
	int i;

	scanf("%d", &T);
	for(ks = 1; ks <= T; ks++)
	{
		scanf("%d", &N);
		for(i = 1; i <= N; i++)
			scanf("%d", &A[i]);
		for(i = 1; i <= N; i++)
			scanf("%d", &B[i]);

		for(i = 1; i <= N; i++)
			sat[i] = u[i] = 0;

		solve(1);

		printf("Case #%d:", ks);
		for(i = 1; i <= N; i++)
			printf(" %d", X[i]);
		printf("\n");
	}

	return 0;
}
