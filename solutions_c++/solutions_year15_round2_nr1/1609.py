#include<cstring>
#include<cstdio>
#include<algorithm>

int ans[1100000],Q[1100000];

inline int Rev(int x)
{
	int tmp = 0;
	while (x)
	{
		(tmp *= 10) += x % 10;
		x /= 10;
	}
	return tmp;
}

void Pre()
{
	int l = 0 , r = 1 , maxn = (int)1e6 , Size = maxn;memset(ans , 255 , sizeof ans);
	Q[1] = 1 , ans[1] = 1;
	while (l < r)
	{
		(l %= Size) ++;
		int now = Q[l];
		int x1 = now + 1 , x2 = Rev(now);
		if (x1 <= maxn) if (ans[x1] == -1) (r %= Size) ++ , Q[r] = x1 , ans[x1] = ans[now] + 1;
		if (x2 <= maxn) if (ans[x2] == -1) (r %= Size) ++ , Q[r] = x2 , ans[x2] = ans[now] + 1;
	}
}

int main()
{
	//freopen("a.in" , "r" , stdin);freopen("a.out" , "w" , stdout);
	Pre();
	int x,T;scanf("%d" , &T);
	
	for (int i = 1 ; i <= T ; i ++) scanf("%d" , &x) , printf("Case #%d: %d\n" , i , ans[x]);
	
}
