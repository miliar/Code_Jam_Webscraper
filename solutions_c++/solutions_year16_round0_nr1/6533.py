#include <iostream>
#include <cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
using namespace std;
typedef long long ll;

int func(int n)
{
	
	int flg = 0;
	int ans = 0,t1,t2=n,tmp;
	while (1)
	{
		tmp = t2;
		while (tmp)
		{

			t1 = tmp % 10;
			flg = (flg | (1 << t1));
			tmp /= 10;
		}
		if (flg == 1023)
		{
			ans = t2;
			break;
		}
		t2 += n;
	}
	return ans;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T,N;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc)
	{
		scanf("%d", &N);
		if (N == 0)
			printf("Case #%d: INSOMNIA\n", tc);
		else
			printf("Case #%d: %d\n",tc, func(N));

	}

	return 0;
}