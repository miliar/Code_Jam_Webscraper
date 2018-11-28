#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;

int a[2000],b[2000],n,T;

int Calc(int x)
{
	int tmp = x;
	for (int i = 1000 ; i > x ; i --) if (a[i])
	{
		int p = i , q;
		if (p % x == 0) q = p / x; else q = p / x + 1;
		q --;
		tmp += a[i] * q;
	}
	return tmp;
}

int main()
{
//	freopen("b.in" , "r" , stdin);freopen("b.out" , "w" , stdout);
	
	int T;
	scanf("%d" , &T);
	
	for (int cnt = 1 ; cnt <= T ; cnt ++)
	{
		memset(a , 0 , sizeof a);
		scanf("%d" , &n);
		int mt = 0 , ans = 1000;
		for (int i = 1 ; i <= n ; i ++) 
		{
			int x;
			scanf("%d" , &x);a[x] ++;
			if (x > mt) mt = x;
		}
		ans = mt;
		for (int i = 1 ; i <= mt ; i ++) ans = min(ans , Calc(i));
		printf("Case #%d: %d\n" , cnt , ans);
	}
	
	return 0;
}
