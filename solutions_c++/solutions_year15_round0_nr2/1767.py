#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

const int MAXN = 1005;

int f[MAXN],A[MAXN],N,cnt;

bool cmp(int a,int b) {return a > b;}

int main()
{
	//freopen("data.in","r",stdin),freopen("data.out","w",stdout);
	int T;
	scanf("%d", &T);
	for(int Ti = 1;Ti <= T;Ti ++)
	{
		memset(A,0,sizeof A);
		N = cnt = 0;
		int Mx = 0,Ans = 1 << 30;
		scanf("%d", &N);
		cnt = N;
		for(int i = 1;i <= N;i ++) scanf("%d", &A[i]),Mx = max(Mx,A[i]);
		for(int Eat = 1;Eat <= Mx;Eat ++)
		{
			memset(f,0,sizeof f);
			for(int i = Eat + 1;i <= Mx;i ++)
			{
				f[i] = 1 << 30;
				for(int j = 1;j < i;j ++)
					f[i] = min(f[i],f[j] + f[i - j] + 1);
			}
			int Sum = 0;
			for(int i = 1;i <= N;i ++) Sum += f[A[i]];
			Ans = min(Ans,Sum + Eat);
		}
		printf("Case #%d: %d\n",Ti, Ans);
	}
}
