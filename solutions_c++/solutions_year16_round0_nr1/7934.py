// #include <bits/stdc++.h>
#include <cstdio>
typedef long long ll;

void solve(int tc)
{
	int n, cnt = 100000;
	ll cur=0, lor;
	unsigned short sudah = 0, tst = ((1<<10)-1);
	scanf("%d", &n);

	while (cnt-- && sudah!=tst)
	{
		lor = (cur += (ll)n);
		while (lor)
		{
			sudah |= (1 << (lor%10));
			lor /= 10LL;
		}
	}

	printf("Case #%d: ", tc);
	if (sudah==tst)
		printf("%lld\n",cur);
	else
		printf("INSOMNIA\n");
}

int main()
{
	// printf("1000001\n");
	// for (int x=0; x<=1000000; ++x) printf("%d\n", x);
	int T;
	scanf("%d", &T);
	for (int x=1; x<=T; ++x) solve(x);
	return 0;
}