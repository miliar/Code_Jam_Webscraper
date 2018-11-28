#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <utility>
#define MAXN 1000005

using namespace std;

int main ()
{
	int T, iT;
	scanf("%d",&T);
	for (iT = 0; iT < T; iT++)
	{
		int N;
		long long P, Q, R, S;
		scanf("%d %I64i %I64i %I64i %I64i",&N,&P,&Q,&R,&S);
		static long long a[MAXN];
		static long long s[MAXN];
		memset(a,0,sizeof(a));
		memset(s,0,sizeof(s));
		int i;
		for (i = 1; i <= N; i++)
		{
			a[i] = (((long long)(i-1) * P + Q) % R) + S;
		}
		for (i = 1; i <= N; i++) s[i] = s[i-1] + a[i];
		int L;
		long long res = 0;
		for (L = 1; L <= N; L++)
		{
			long long lp = s[L-1];
			int l, r, c;
			l = L; r = N;
			while (r > l)
			{
				c = (l+r)/2;
				if ((s[c] - s[L-1]) >= (s[N] - s[c])) r = c;
				else l = c+1;
			}
			c = l;
			long long rp = max(s[c] - s[L-1], s[N] - s[c]);
			if (c != L)
			{
				c--;
				rp = min(rp, max(s[c] - s[L-1], s[N] - s[c]));
			}
			long long ans = s[N] - max(lp, rp);
			if (ans > res) res = ans;
		}
		printf("Case #%d: %.10lf\n",iT+1,(double)(res) / (double)(s[N]));
	}
	return 0;
}
