#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 205;

int N,K;
int Ch[MAXN];
double F[MAXN][MAXN * 2],P[MAXN],Ans;

void Update(double &x,double y)
{
	x = (x > y ? x : y);
}

void Test()
{
	memset(F,0,sizeof F);
	F[0][K] = 1;
	for(int i = 1;i <= K;i ++)
	{
		int ref = Ch[i];
		for(int j = 0;j <= 2 * K;j ++)
		{
			if (j > 0) F[i][j] += F[i - 1][j - 1] * P[ref];
			if (j < 2 * K) F[i][j] += F[i - 1][j + 1] * (1 - P[ref]);
		}
	}
	Ans = max(Ans,F[K][K]);
}

void Work(int Case)
{
	printf("Case #%d: ", Case);
	scanf("%d%d", &N, &K);
	memset(F,0,sizeof F);
	for(int i = 1;i <= N;i ++) scanf("%lf", &P[i]);
	sort(P + 1,P + N + 1);
	Ans = 0;
	for(int i = 0;i <= K;i ++)
	{
		for(int j = 1;j <= i;j ++) Ch[j] = j;
		for(int j = 1;j <= K - i;j ++) Ch[j + i] = N - j + 1;
		Test();
	}
	printf("%.10f\n", Ans);
}

int main()
{
	freopen("data.in","r",stdin),freopen("data.out","w",stdout);
	int T;
	scanf("%d", &T);
	for(int i = 1;i <= T;i ++) Work(i);
	return 0;
}
