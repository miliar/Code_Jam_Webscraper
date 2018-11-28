#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
	//freopen("data.in","r",stdin),freopen("data.out","w",stdout);
	int T;
	scanf("%d", &T);
	for(int i = 1;i <= T;i ++)
	{
		int S,Cur = 0,Ans = 0;scanf("%d", &S);
		for(int j = 0;j <= S;j ++)
		{
			char c;
			while (c = getchar(),c < '0' || c > '9');
			int p = c - 48;
			if (Cur < j) Ans += j - Cur,Cur += j - Cur;
			Cur += p;
		}
		printf("Case #%d: %d\n",i, Ans);
	}
}
