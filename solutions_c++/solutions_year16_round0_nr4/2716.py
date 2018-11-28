#include <bits/stdc++.h>
using namespace std;
long long xp(int b, int i)
{
	if(i == 0) return 1;
	if(i == 1) return b;
	long long x = xp(b, i/2);
	x *= x;
	if(i&1) x*= b;
	return x;
}
int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for(int qq = 1; qq<= tt; qq++)
	{
		int k, c, s;
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d: ", qq);
		for(int i = 0; i< k; i++)
		{
			printf("%lld ", i*xp(k, c-1)+1);
		}
		printf("\n");
	}
}