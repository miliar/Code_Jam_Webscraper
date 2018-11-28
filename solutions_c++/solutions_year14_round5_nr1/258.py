#include <vector>
#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>

using namespace std;

int n, p, q, r, s;
long long S[1000010];

double Work()
{
	scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
	S[0] = q % r + s;
	for (long long i = 1; i < n; i ++)
		S[i] = S[i-1] + (i*p+q) % r + s;
	int ll, rr, mid;
	long long ret = S[n-1];
	for (int b = 0; b < n; b ++)
	{
		long long base = S[n-1] - S[b], z = S[b];
		
		ll = 0; rr = b;
		while (ll < rr)
		{
			mid = (ll + rr) / 2;
			z = min(z, max(S[mid], S[b] - S[mid]));
			if (S[mid] * 2 > S[b]) rr = mid;
			else ll = mid + 1;
		}
		z = min(z, max(S[ll], S[b] - S[ll]));
		ret = min(ret, max(base, z));
	}
	return (ret + 0.0) / S[n-1];
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++)
		printf("Case #%d: %.10f\n", t, 1 - Work());
	return 0;
}