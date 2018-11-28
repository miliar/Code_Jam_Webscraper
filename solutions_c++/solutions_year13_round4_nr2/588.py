#include <cstdio>

int main(void)
{
	int T;
	scanf("%d", &T);
	for(int caseN=1;caseN<=T;caseN++)
	{
		long long n, p;
		scanf("%lld %lld", &n, &p);
		printf("Case #%d: ", caseN);
		long long s = 0, e = (1LL << n), mid, ans;
		while(s < e)
		{
			mid = (s + e) / 2;
			int canLose = 0;
			long long cur = 2;
			while(cur - 1 <= mid)
			{
				canLose++;
				cur *= 2;
			}

			long long tar = 1;
			long long temp = (1LL << (n - 1));
			for(int i=0;i<canLose;i++)
			{
				tar += temp;
				temp /= 2;
			}

			if(tar <= p) { s = mid + 1; ans = mid; }
			else e = mid;
		}

		printf("%lld ", ans);

		s = 0, e = (1LL << n);
		while(s < e)
		{
			mid = (s + e) / 2;
			int canWin = 0;
			long long cur = 2;
			while(cur - 1 <= ((1LL << n) - mid - 1))
			{
				canWin++;
				cur *= 2;
			}

			long long tar = (1LL << (n - canWin));
			if(tar <= p) { s = mid + 1; ans = mid; }
			else e = mid;
		}

		printf("%lld\n", ans);
	}

	return 0;
}
