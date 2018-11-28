#include <algorithm>
#include <cstdio>
using namespace std;

int T;
int E, R, N;
int v[100];
int en[100];

int back(int l, int e);

int main()
{
	scanf("%d", &T);

	for(int q=1; q<=T; q++) {
		scanf("%d%d%d", &E, &R, &N);
		for(int i=0; i<N; i++) scanf("%d", &v[i]);
		printf("Case #%d: %d\n", q, back(0, E));
	}

	return 0;
}

int back(int l, int e)
{
	if(l==N) return 0;
	int best=0;
	for(int i=0; i<=e; i++) {
		int akt=i*v[l]+back(l+1, min(e-i+R, E));
		best=max(best, akt);
	}
	return best;
}
