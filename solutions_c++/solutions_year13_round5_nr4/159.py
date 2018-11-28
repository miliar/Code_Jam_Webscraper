#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

typedef long double K;

K DP[10000000];
char buf[50];
int n,M;

int wait(int mask, int pos)
{
	for(int i = 0;i<n;i++)
		if((mask) & (1 << ((pos + i)%n)))
			return i;
}
void getDP(int mask)
{
	DP[mask] = 0.0;
	for(int i = 0;i<n;i++)
		DP[mask] += n - wait(mask,i) + DP[mask - (1 << ((i + wait(mask,i))%n))];
	DP[mask] /= n;
}
void read()
{
	scanf("%s", buf);
	n = strlen(buf);
	M = 0;
	for(int i = 0;i<n;i++)
		if(buf[i] == '.')
			M += (1 << i);
}
void solve(int tc)
{
	DP[0] = 0.0;
	for(int i = 1;i<(1 << n);i++)
		getDP(i);
	printf("Case #%d: %.10Lf\n", tc, DP[M]);
}
int main()
{
	int Z;
	scanf("%d", &Z);
	for(int i = 1;i<=Z;i++)
	{
		read();
		solve(i);
	}
}

