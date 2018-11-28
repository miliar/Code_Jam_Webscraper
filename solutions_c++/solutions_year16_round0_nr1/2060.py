


#include<iostream>
#include<vector>
using namespace std;

typedef long long ll;

int main()
{
	//freopen("A.in", "r", stdin);
	//freopen("A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		ll N;
		scanf("%lld", &N);
		printf("Case #%d: ", cases);
		if (N == 0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		vector<bool> v(10, false);
		int cnt = 0;
		ll ans = 0;
		for (int n = N; n <= N * 1000000; n += N)
		{
			ll t = n;
			while (t > 0)
			{
				int l = t % 10;
				if (!v[l])
				{
					v[l] = true;
					cnt++;
				}

				t /= 10;
			}
			if (cnt == 10)
			{
				ans = n;
				break;
			}
		}
		if (!ans)
			printf("INSOMNIA\n");
		else
			printf("%lld\n", ans);
	}

	//system("pause");
	return 0;
}