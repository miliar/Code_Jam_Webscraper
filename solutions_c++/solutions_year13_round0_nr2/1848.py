#include <algorithm>
#include <cstdio>

using namespace std;

int B[105][105];
int MC[105];
int MR[105];
int N,M;

void read()
{
	scanf("%d%d", &N, &M);
	for(int i = 0;i<N;i++)
		for(int j = 0;j<M;j++)
			scanf("%d", &B[i][j]);
	for(int i = 0;i<max(N,M);i++)
		MC[i] = MR[i] = 0;
	for(int i = 0;i<N;i++)
		for(int j = 0;j<M;j++)
		{
			MR[i] = max(MR[i], B[i][j]);
			MC[j] = max(MC[j], B[i][j]);
		}
}
bool check()
{
	for(int i = 0;i<N;i++)
		for(int j = 0;j<M;j++)
			if(B[i][j] < MR[i] && B[i][j] < MC[j])
				return false;
	return true;
}
void solve(int tc)
{
	if(check())
		printf("Case #%d: YES\n", tc);
	else
		printf("Case #%d: NO\n", tc);
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
	return 0;
}
