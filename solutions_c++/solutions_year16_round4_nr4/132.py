#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 5;

char S[MAXN];
bool Ch[MAXN][MAXN],Pick[MAXN],Out[MAXN],ok;
int Ord[MAXN],P[MAXN],N,Ans;

void Calc(int Now)
{
	if (Now > N) return;
	bool ch = 0;
	for(int i = 1;i <= N;i ++)
		if (Ch[P[Now]][i] && !Out[i])
		{
			Out[i] = 1;
			Calc(Now + 1);
			Out[i] = 0;
			ch = 1;
			if (!ok) return;
		}
	if (!ch) ok = 0;
}

void Go(int Now)
{
	if (!ok) return;
	if (Now > N) Calc(1); else
	{
		for(int i = 1;i <= N;i ++)
			if (!Pick[i])
			{
				Pick[i] = 1,P[Now] = i;
				Go(Now + 1);
				Pick[i] = 0;
			}
	}
}

void Test(int d)
{
	ok = 1;
	Go(1);
	if (ok) 
		Ans = min(Ans,d);
}

void Dfs(int x,int y,int c)
{
	if (c >= Ans) return;
	if (x > N) {Test(c);return;}
	if (y > N) {Dfs(x + 1,1,c);return;}
	if (Ch[x][y] == 1) {Dfs(x,y + 1,c);return;}
	for(int i = 0;i < 2;i ++)
	{
		Ch[x][y] = i;
		Dfs(x,y + 1,c + i);
		Ch[x][y] = 0;
	}
}

void Work(int Case)
{
	printf("Case #%d: ", Case);
	scanf("%d", &N);
	for(int i = 1;i <= N;i ++)
	{
		scanf("%s", S + 1);
		for(int j = 1;j <= N;j ++)
			Ch[i][j] = (S[j] == '1');
	}
	Ans = (1 << 30);
	Dfs(1,1,0);
	printf("%d\n", Ans);
}

int main()
{
	freopen("data.in","r",stdin),freopen("data.out","w",stdout);
	int T;
	scanf("%d", &T);
	for(int i = 1;i <= T;i ++) Work(i);
	return 0;
}
