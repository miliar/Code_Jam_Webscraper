#include <bits/stdc++.h>
using namespace std;

int N, K;
double Pb[30];
double P[30]; //P i sukcesów
double P2[30];
void solver()
{
	scanf("%d%d", &N, &K);
	for(int i = 0; i < N; ++i)
		scanf("%lf", &Pb[i]);
	int MAX = 1 << N;
	double Maxp = 0;
	for(int i = 0; i < MAX; ++i)
		if(__builtin_popcount(i) == K)
		{
			P[0] = 1;
			for(int j = 1; j < N; ++j) P[j] = 0;
			for(int j = 0; j < N; ++j)
				if(i & (1 << j))
				{
					P2[0] = 0;
					for(int k = 0; k < N; ++k)
					{
						P2[k] += P[k]*(1-Pb[j]);
						P2[k+1] = P[k]*Pb[j];
					}
					for(int k = 0; k < N; ++k)
						P[k] = P2[k];
				}
			Maxp = max(Maxp, P[K/2]);
		}
	printf("%.9f", Maxp);
}
int main()
{
	ios_base::sync_with_stdio(0);
	//solver();
	//return 0;
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		solver();
		puts("");
	}
	
	
	return 0;
}
