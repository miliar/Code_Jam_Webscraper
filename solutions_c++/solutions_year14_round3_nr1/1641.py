#include <cstdio>

int gcd(long long a, long long b)
{
	if(b == 0)
		return a;
	return gcd(b, a % b);
}

int isp2(int a)
{
	while(a > 1){
		if(a % 2 == 0)
			a /= 2;
		else
			return 0;
	}
	return 1;
}

int main()
{
	int t, caseNum = 1, ans;
	long long p, q, gg;
	scanf("%d", &t);
	while(t--){
		scanf("%I64d/%I64d", &p, &q);
		gg = gcd(p, q);
		p /= gg;
		q /= gg;
		if(isp2(q) == 0)
			ans = -1;
		else{
			ans = 1;
			while(p < q / 2 && q > 1){
				q /= 2;
				ans++;
			}
		}
		if(ans == -1)
			printf("Case #%d: impossible\n", caseNum++);
		else
			printf("Case #%d: %d\n", caseNum++, ans);
	}
	return 0;
}
